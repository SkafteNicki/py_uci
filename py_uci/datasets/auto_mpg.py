# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:49:43 2019

@author: nsde
"""

#%%
import pandas as pd
import numpy as np
from ..base import Dataset
from ..utility import convert_to_numeric

#%%
class auto_mpg(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'auto-mpg.data' in f:
                df = pd.read_csv(f, delim_whitespace=True, header=None)
        df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
                      'weight', 'acceleration', 'model year', 'origin',
                      'car name']
        self.dataframe = df
        
    @property
    def data(self):
        return self.dataframe.values[:,1:-1].astype('float32')
    
    @property
    def target(self):
        return convert_to_numeric(self.dataframe.values[:,0])