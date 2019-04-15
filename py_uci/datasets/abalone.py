# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:57:19 2019

@author: nsde
"""

#%%
import pandas as pd
import numpy as np
from ..base import Dataset
from ..utility import convert_to_numeric

#%%
class abalone(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'abalone.data' in f:
                df = pd.read_csv(f, sep=',', header=None)
        df.columns = ['Sex', 'Length', 'Diameter', 'Hight', 'Whole weight',
                      'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
        self.dataframe = df
        
    @property
    def data(self):
        first_c = convert_to_numeric(self.dataframe.values[:,0]).reshape(-1, 1)
        rest = self.dataframe.values[:,1:-1].astype('float32')
        return np.concatenate([first_c, rest], axis=1)
