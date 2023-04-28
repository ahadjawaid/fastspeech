# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_modules.ipynb.

# %% auto 0
__all__ = ['get_positional_embeddings', 'MultiHeadAttention', 'ConvNetwork', 'FeedForwardTransformer', 'FFTConfig',
           'DurationPredictor', 'DPConfig', 'length_regulator', 'FastSpeech']

# %% ../nbs/01_modules.ipynb 3
import torch
import torch.nn as nn
from torch import tensor
import math
from einops import rearrange
import torch.nn.functional as F

# %% ../nbs/01_modules.ipynb 12
def get_positional_embeddings(seq_len, # The length of the sequence
                              d_model, # The hidden dimension of the model
                              device: torch.device =None): # Device you want to use
    pos = torch.arange(d_model, device=device)[None, :]
    i = torch.arange(seq_len, device=device)[:, None]
    angle = pos / torch.pow(10000, 2 * i / d_model)
    pos_emb = torch.zeros(angle.shape, device=device)
    pos_emb[0::2,:], pos_emb[1::2,:] = angle[0::2,:].sin(), angle[1::2,:].cos()
    return pos_emb

# %% ../nbs/01_modules.ipynb 22
class MultiHeadAttention(nn.Module):
    '''The Multi-Head Attention component comes from the 
    [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper. 
    For the purpose of simplicity we combine the two parts of the Multi-Headed Attention 
    into one module'''
    def __init__(self, 
                 ni: int, # The input dimension 
                 nh: int): # The number of attention heads
        ''''''
        super().__init__()
        self.nh = nh
        self.scale = math.sqrt(ni / nh)
        self.kqv = Linear(ni, ni*3)
        self.proj = Linear(ni, ni)
        
    def forward(self, inp: tensor):
        x = self.kqv(inp)
        x = rearrange(x, 'n s (h d) -> (n h) s d', h=self.nh)
        
        Q, K, V = torch.chunk(x, 3, dim=-1)
        x = F.softmax(Q @ K.transpose(1,2) / self.scale, dim=-1) @ V
    
        x = rearrange(x, '(n h) s d -> n s (h d)', h=self.nh)
        x = self.proj(x)
        return x

# %% ../nbs/01_modules.ipynb 25
class ConvNetwork(nn.Module):
    '''The Convolution network consists of two Conv1D layers with the 
    intermediate dimension being named the filter size.'''
    def __init__(self, 
                 ni: int, # Input dimension 
                 fs: int, # Filter size for intermediate dimension
                 ks: list[int]): # A two element array of kernal sizes
        ''''''
        super().__init__()
        assert len(ks) == 2
        padding = list(map(lambda x: (x - 1) // 2, ks))
        self.layers = nn.ModuleList([Conv1d(ni, fs, ks[0], padding=padding[0]),
                                     Conv1d(fs, ni, ks[1], padding=padding[1])])
        
    def forward(self, inp: tensor):
        x = inp.transpose(1,2)
        for layer in self.layers:
            x = F.relu(layer(x))
        return x.transpose(1,2)

# %% ../nbs/01_modules.ipynb 28
class FeedForwardTransformer(nn.Module):
    ''''''
    def __init__(self, 
                 ni: int, # Input dimension
                 nh: int, # Number of attention heads
                 fs: int, # Filter size for intermediate dimension
                 ks: list[int], # A two element list of kernal sizes
                 p: list[float]): # A two element list of dropout probabilities
        '''This module consists of a MultiHeadAttention, and ConvNetwork layer with 
        dropout, residuals, and layer normalization being applied after each layer'''
        super().__init__()
        assert len(ks) == 2 and len(p) == 2
        self.layers = nn.ModuleList([MultiHeadAttention(ni, nh), ConvNetwork(ni, fs, ks)])
        self.norms = nn.ModuleList([nn.LayerNorm(ni) for _ in range(2)])
        self.dropouts = nn.ModuleList([nn.Dropout(p[i]) for i in range(2)])
        
    def forward(self, inp: tensor):
        res = inp
        modules = zip(self.layers, self.norms, self.dropouts)
        for layer, norm, dropout in modules:
            x = layer(res)
            x = norm(dropout(x) + res)
            res = x
        return x

# %% ../nbs/01_modules.ipynb 29
class FFTConfig:
    '''To allow for easily configurable FFT modules we decided to create a FFTConfig
    to allow for more readable, and customizable code when creating FFT'''
    def __init__(self, 
                 ni: int, # The input size
                 nh: int, # The number of attention heads
                 fs: int, # Filter size for intermediate dimension
                 ks: list[int], # A two element list of kernal sizes
                 p: list[float]): # A two element list of dropout probabilities
        self.ni, self.nh, self.fs, self.ks, self.p = ni, nh, fs, ks, p
    
    def build(self):
        return FeedForwardTransformer(self.ni, self.nh, self.fs, self.ks, self.p)

# %% ../nbs/01_modules.ipynb 33
class DurationPredictor(nn.Module):
    '''This module predicts the logarithmic duration length for each phoneme 
    based on the phoneme hidden features. It consists of 2-layer 1D convolutional network 
    with ReLU activation, each followed by the layer normalization and the dropout layer, 
    and an extra linear layer to output a scalar.'''
    def __init__(self, 
                 ni: int, # Input dimension
                 fs: int, # Filter size for intermediate dimension
                 ks: list[int], # A two element list of kernal sizes
                 p: list[float]): # A two element list of dropout probabilities
        ''''''
        super().__init__()
        assert len(ks) == 2 and len(p) == 2
        
        padding = list(map(lambda x: (x - 1) // 2, ks))
        self.layers = nn.ModuleList([Conv1d(ni, fs, ks[0], padding=padding[0]),
                                     Conv1d(fs, ni, ks[1], padding=padding[1])])
        self.norms = nn.ModuleList([nn.LayerNorm(sz) for sz in [fs, ni]])
        self.dropouts = nn.ModuleList([nn.Dropout(p[i]) for i in range(2)])
        self.linear = Linear(ni, 1)
    
    def forward(self, hi: tensor):
        x = hi
        modules = zip(self.layers, self.norms, self.dropouts)
        for layer, norm, dropout in modules:
            x = layer(x.transpose(1, 2))
            x = dropout(F.relu(x))
            x = norm(x.transpose(1,2))
        x = self.linear(x)
        return x.squeeze()

# %% ../nbs/01_modules.ipynb 34
class DPConfig:
    '''To allow for easily configurable Deration Predictor modules we 
    decided to create a DPConfig to allow for more readable, 
    and customizable code when creating Duration Predcitor modules'''
    def __init__(self, 
                 ni: int, # Input dimension
                 fs: int, # Filter size for intermediate dimension
                 ks: list[int], # A two element list of kernal sizes
                 p: list[float]): # A two element list of dropout probabilities
        self.ni, self.fs, self.ks, self.p = ni, fs, ks, p
    
    def build(self):
        return DurationPredictor(self.ni, self.fs, self.ks, self.p)

# %% ../nbs/01_modules.ipynb 38
def length_regulator(hi: tensor, # The hidden phoneme features
                     durations: tensor, # The phoneme durations to upsample to
                     upsample_ratio: float, # The multiplier ratio of upsampling rate
                     device: torch.device = None): # Device you want to use
    assert len(durations.sum(dim=1).unique()) == 1
    durations = (upsample_ratio * durations).to(torch.int)
    
    (bs, _, nh), sl = hi.shape, durations[0].sum().item()
    
    ho = torch.zeros((bs, sl, nh), device=device)
    for i in range(bs):
        ho[i] = hi[i].repeat_interleave(durations[i], dim=0)
    return ho

# %% ../nbs/01_modules.ipynb 42
class FastSpeech(nn.Module):
    ''''''
    def __init__(self, 
                 ne: int, # Number of embeddings (vocab size) 
                 ni: int, # The number of hidden dimension
                 no: int, # The number of outputs bins (mel bins)
                 ec: FFTConfig, # Encoder config 
                 enb: int, # The number of FFT in encoder
                 dc: FFTConfig, # Decoder config
                 dnb: int, #The number of FFT in decoder
                 dpc: DPConfig, # Duration Predictor config
                 device=None):
        ''''''
        super().__init__()
        self.device = device
        self.embedding = nn.Embedding(ne, ni)
        self.encoder = nn.Sequential(*[ec.build() for _ in range(enb)])
        self.decoder = nn.Sequential(*[dc.build() for _ in range(dnb)])
        self.duration_predictor = dpc.build()
        self.linear = Linear(ni, no)
        
    def forward(self, inp: tensor, # The input phonemes in vectorized form
                durations: tensor = None, # The phoneme durations, used for training
                upsample_ratio: float = 1.): # Upsampling ratio (adjust speed of speech)
        x = self.embedding(inp)
        x = x +  get_positional_embeddings(*x.shape[-2:], device=self.device)
        x = self.encoder(x)

        log_durations = self.duration_predictor(x.detach())
        if durations == None or not self.training:
            durations = log_durations.exp()
        x = length_regulator(x, durations, upsample_ratio, device=self.device)
        
        x = x +  get_positional_embeddings(*x.shape[-2:], device=self.device)
        x = self.decoder(x)
        x = self.linear(x).transpose(1,2)
        
        return (x, log_durations) if self.training else x        
