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
    def _formatter(self):
        for f in self.files:
            if 'winequality-red.csv' in f:
                df_red = pd.read_csv(f, sep=';')
            if 'winequality-white.csv' in f:
                df_white = pd.read_csv(f, sep=';')
        df_full = pd.concat([df_red, df_white], axis=0)
        self.data = df_full.values.astype('float32')
        self.attribute_names = list(df_red)
        self.labels = ['red', 'white']
        self.target = np.concatenate([np.zeros((len(df_red),)), 
                                      np.ones((len(df_white),))]).astype('int32')
        self.dataframe = df_full
        self.dataframe['type'] = np.array(self.labels)[self.target]
        
#%%        
class wine_red(Dataset):    
    def _formatter(self):
        for f in self.files:
            if 'winequality-red.csv' in f:
                df = pd.read_csv(f, sep=';')
        self.dataframe = df
        self.data = df.values[:,:-1].astype('float32')
        self.attribute_names = list(df)
        self.target = df.values[:,-1].astype('float32')
    
#%%        
class wine_white(Dataset):   
    def _formatter(self):
        for f in self.files:
            if 'winequality-white.csv' in f:
                df = pd.read_csv(f, sep=';')
        self.dataframe = df
        self.data = df.values[:,:-1].astype('float32')
        self.attribute_names = list(df)
        self.target = df.values[:,-1].astype('float32')