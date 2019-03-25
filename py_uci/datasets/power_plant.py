# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:00:10 2019

@author: nsde
"""

#%%
import pandas as pd
from .base import Dataset
import zipfile, os

#%%
class power_plant(Dataset):
    def _create_dataframe(self):
        # Extract .zip file
        for f in self.files:
            if 'CCPP.zip' in f:
                zipref = zipfile.ZipFile(f, 'r')
                zipref.extractall('/'.join(f.split('/')[:-1]))
                zipref.close()
        
        self._update_files_list()
        
        # Move files from folder to data folder
        for f in self.files:
            if os.path.isdir(f):
                for ff in os.listdir(f):
                    old = f + '/' + ff
                    new = '/'.join(f.split('/')[:-1]) + '/' + ff.split('/')[-1]
                    os.rename(old, new)

        self._update_files_list()
        
        # Get dataframe
        for f in self.files:
            if 'Folds5x2_pp.xlsx' in f:
                df = pd.read_excel(f)
        self.dataframe = df
