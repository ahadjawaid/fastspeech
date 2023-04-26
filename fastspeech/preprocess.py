# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_preprocess.ipynb.

# %% auto 0
__all__ = ['Vocab', 'trim_audio']

# %% ../nbs/04_preprocess.ipynb 3
from pathlib import Path
import librosa

# %% ../nbs/04_preprocess.ipynb 7
class Vocab:
    '''This is a vocab object to used to load in a vocabulary, vectorize phonemes, and decode embeddings'''
    def __init__(self, 
                 vocab_path: str, # The path to vocabulary file containing all the words in the vocabulary
                 specials: list =[]): # The special tokens not in the vocabulary file
        pad_token = "<pad>"
        self.vocab = self._load_vocab(vocab_path) + [pad_token] + specials
        self.tok2idx = {tok: i for i, tok in enumerate(self.vocab)}
        self.pad_num = self.tok2idx[pad_token]
    
    def __getitem__(self, val: int|str): # The token string or the vectorized integer
        val_type = type(val)
        if val_type == int and val < len(self.vocab): 
            return self.vocab[val]
        elif val_type == str:
            return self.tok2idx[val]
        else:
            raise Exception(f"Used the wrong type: {val_type}")
        
    def __len__(self):
        return len(self.vocab)
        
    def _load_vocab(self, vocab_path: str): # The path to the phoneme vocab list
        lines = Path(vocab_path).open().readlines()
        return list(map(lambda x: x.strip(), lines))

# %% ../nbs/04_preprocess.ipynb 10
def trim_audio(inp, # Input audio array
               top_db, # The threshold (in decibels) below reference to consider as silence
               n_fft, # The number of samples per analysis frame
               hl): # The number of samples between analysis frames
    audio, _  = librosa.effects.trim(y=inp, top_db=top_db, frame_length=n_fft, hop_length=hl)
    return audio
