# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:22:30 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset
import zipfile

#%%
class superconduct(Dataset):
    def _create_dataframe(self):
        # Extract .zip file
        for f in self.files:
            if 'superconduct.zip' in f:
                zipref = zipfile.ZipFile(f, 'r')
                zipref.extractall('/'.join(f.split('/')[:-1]))
                zipref.close()
        
        self._update_files_list()
               
        # Get dataframe
        for f in self.files:
            if 'train.csv' in f:
                df = pd.read_csv(f)
        self.dataframe = df
