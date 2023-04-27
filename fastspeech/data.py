# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_data.ipynb.

# %% auto 0
__all__ = ['collate_fn']

# %% ../nbs/05_data.ipynb 3
from .loading import *
from .preprocess import *
from torch.utils.data import Dataset, DataLoader
from torch import tensor
import torch
from functools import partial
from fastcore.foundation import L

# %% ../nbs/05_data.ipynb 8
def collate_fn(inp, pad_num: int):
    phones, durations, mels = zip(*inp)
    
    mel_batched, phones_batched = pad_mels(mels), pad_phones(phones, pad_num)
    duration_batched = pad_duration(durations, mel_batched.shape[-1])
    
    return phones_batched, duration_batched, mel_batched
