# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:58:55 2019

@author: nsde
"""

#%%
import pandas as pd
from .base import Dataset
from ..utility import convert_to_numeric

#%%
class forest_fire(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'forestfires.csv' in f:
                df = pd.read_csv(f)
        self.dataframe = df
        
    @property
    def data(self):
        data = self.dataframe.values[:,:-1]
        data[:,2] = convert_to_numeric(data[:,2])
        data[:,3] = convert_to_numeric(data[:,3])
        return data.astype('float32')
    
    
