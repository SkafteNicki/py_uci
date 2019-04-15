# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:15:42 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset

#%%
class concrete(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'Concrete_Data.xls' in f:
                df = pd.read_excel(f)
        self.dataframe = df

