# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:31:32 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset

#%%
class boston(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'housing.data' in f:
                df = pd.read_csv(f, delim_whitespace=True)
        self.dataframe = df        
        self.dataframe.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
                                  'NOX', 'RM', 'AGE', 'DIS', 'RAD',
                                  'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']