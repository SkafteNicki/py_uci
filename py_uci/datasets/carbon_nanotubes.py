# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:44:10 2019

@author: nsde
"""

#%%
import pandas as pd
from .base import Dataset

#%%
class carbon_nanotubes(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'carbon_nanotubes.csv' in f:
                df = pd.read_csv(f, sep=';')
        self.dataframe = df
