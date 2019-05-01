# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:26:13 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset

#%%
class airfoil(Dataset):
    def _create_dataframe(self):
        # Get dataframe
        for f in self.files:
            if 'airfoil_self_noise.dat' in f:
                df = pd.read_csv(f, header=None, delim_whitespace=True)
        self.dataframe = df
        