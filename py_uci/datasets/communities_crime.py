# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:52:19 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset
import zipfile

#%%
class communities_crime(Dataset):
    def _create_dataframe(self):
        # Get dataframe
        for f in self.files:
            if 'communities.data' in f:
                df = pd.read_csv(f, header=None)
        self.dataframe = df
        