# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:31:32 2019

@author: nsde
"""

#%%
import pandas as pd
import numpy as np
from .base import Dataset
from ..utility import convert_to_numeric

#%%
class boston(Dataset):
    def _formatter(self):
        for f in self.files:
            if 'housing.data' in f:
                df = pd.read_csv(f, delim_whitespace=True)
        self.dataframe = df        
        self.attribute_name = ['CRIM', 'ZN', 'INDUS', 'CHAS',
                               'NOX', 'RM', 'AGE', 'DIS', 'RAD',
                               'TAX', 'PTRATIO', 'B', 'LSTAT']
        self.data = df.values[:,:-1].astype('float32')
        self.target = df.values[:,-1].astype('float32')