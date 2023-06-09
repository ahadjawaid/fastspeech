# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_data.ipynb.

# %% auto 0
__all__ = ['compute_statistics', 'TTSDataset', 'collate_fn']

# %% ../nbs/05_data.ipynb 3
from .loading import *
from .preprocess import *
from torch.utils.data import Dataset, DataLoader
from torch import tensor
import torch
from functools import partial
from fastcore.foundation import L

# %% ../nbs/05_data.ipynb 5
def compute_statistics(data: list[tensor]):
    flat = flatten_and_concat(data)
    return {"min_val": flat.min(), "max_val": flat.max(), 
            "mean": flat.mean(), "std": flat.std()}

# %% ../nbs/05_data.ipynb 6
class TTSDataset(Dataset):
    def __init__(self, 
                 path_data: str, 
                 path_vocab: str, 
                 Norm, # A Normalization class
                 sr: int=22050, # Sampling rate
                 n_fft: int=1024, # Length of the windowed signal
                 hl: int=256, # The hop length
                 nb: int=80, # Number of mel bins
                 ds: slice=slice(None), # The data slice
                 stats: dict={}, # Statistics dictionary for preprocessing
                 preload: bool=False): # Loads dataset on initilzation
        
        self.preload = preload
        self.stats = stats
        
        replace_to_tg = partial(replace_extension, extension=".TextGrid")
        self.load_audio = partial(load_audio, sr=sr)
        self.melspectrogram = partial(melspectrogram, n_fft=n_fft, hl=hl, nb=nb)
        self.get_phones_and_durations = partial(get_phones_and_durations, sr=sr, hl=hl)
        self.norm = Norm(**stats)
        
        self.files = get_audio_files(path_data)[ds]
        self.files_tg = self.files.map(replace_to_tg)
        
        self.vocab = Vocab(path_vocab, ["spn"])
        
        self.pho_transform = [partial(phones_list_to_num, vocab=self.vocab)]
        self.wav_transfom = [partial(trim_audio, top_db=self.stats["top_db"], 
                             n_fft=n_fft, hl=hl)]
        self.mel_tranform = [self.norm.normalize]
        
        
        if preload:
            self.wavs = self.files.map(self.load_audio)
            self.wavs = self.wavs.map(partial(transform_inp, 
                                              transform_list=self.wav_transfom))

            self.pitch = map_tensors(self.wavs.map(extract_pitch))
            self.energy = map_tensors(self.wavs.map(extract_energy))
            
#             self.pitch_stats = compute_statistics(self.pitch)
#             self.energy_stats = compute_statistics(self.energy)
            
#             self.quantize_pitch = partial(linear_quantization, n_bins=256, min_v=self.pitch_stats["min_val"],
#                                           max_v=self.pitch_stats["max_val"])
#             self.quantize_energy = partial(linear_quantization, n_bins=256, min_v=self.energy_stats["min_val"],
#                                            max_v=self.energy_stats["max_val"])
            
#             self.pitch = map_tensors(self.pitch.map(self.quantize_pitch))
#             self.energy = map_tensors(self.energy.map(self.quantize_energy))
            
            self.phones, self.durations = zip(*self.files_tg.map(
                                              self.get_phones_and_durations))
            
            self.phones = map_tensors(transform_inp(self.phones, self.pho_transform))
            
            self.mels = map_tensors(self.wavs.map(self.melspectrogram).map(
                        transform_inp, transform_list=self.mel_tranform))
            mel_lens = list(map(lambda x: x.shape[-1], self.mels))
            
            self.durations = [round_and_align_durations(d, mel_lens[i]) 
                              for i, d in enumerate(map_tensors(self.durations))]
    def __getitem__(self, idx):
        if self.preload:
            return self.phones[idx], self.durations[idx], self.pitch[idx], self.energy[idx], self.mels[idx]
        
        wav = transform_inp(self.load_audio(self.files[0]), self.wav_transfom)
        mel = tensor(transform_inp(self.melspectrogram(wav), self.mel_tranform))
        
        phones, duration = self.get_phones_and_durations(self.files_tg[idx])
        phones = tensor(transform_inp(phones, self.pho_transform)).squeeze()

        duration = round_and_align_durations(tensor(duration), mel.shape[-1])
        
        return phones, duration, mel
    
    def __len__(self):
        return len(self.files)

# %% ../nbs/05_data.ipynb 9
def collate_fn(inp, pad_num: int, norm):
    phones, durations, pitch, energy, mels = zip(*inp)
    norm_zero = norm.normalize(0)
    
    mel_batched = pad_mels(mels, norm_zero)
    phones_batched = pad_phones(pad_max_seq(phones), pad_num)
    pitch_batched = pad_phones(pitch, 0)
    energy_batched = pad_phones(energy, 0)
    mel_len = mel_batched.shape[-1]
    
    duration_batched = pad_duration(pad_max_seq(durations), mel_batched.shape[-1])
    
    assert phones_batched.shape == duration_batched.shape
    assert len(duration_batched.sum(dim=1).unique()) == 1
    return phones_batched, duration_batched, pitch_batched, energy_batched, mel_batched
