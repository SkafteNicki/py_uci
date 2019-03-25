#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:04:24 2019

@author: nsde
"""

#%%
import pandas as pd
import numpy as np
from .base import Dataset

#%%
class wine_quality(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'winequality-red.csv' in f:
                df_red = pd.read_csv(f, sep=';')
            if 'winequality-white.csv' in f:
                df_white = pd.read_csv(f, sep=';')
        self.dataframe = pd.concat([df_red, df_white], axis=0)
        self.dataframe['type'] = [*(len(df_red)*['red']), *(len(df_white)*['white'])]
        
#%%        
class wine_red(Dataset):    
    def _create_dataframe(self):
        for f in self.files:
            if 'winequality-red.csv' in f:
                df = pd.read_csv(f, sep=';')
        self.dataframe = df
    
#%%        
class wine_white(Dataset):   
    def _create_dataframe(self):
        for f in self.files:
            if 'winequality-white.csv' in f:
                df = pd.read_csv(f, sep=';')
        self.dataframe = df
