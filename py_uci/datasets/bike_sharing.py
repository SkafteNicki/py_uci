# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:50:56 2019

@author: nsde
"""

#%%
import pandas as pd
from .base import Dataset
import zipfile

#%%
class bike_sharing(Dataset):
    def _create_dataframe(self):
        # Extract .zip file
        for f in self.files:
            if 'Bike-Sharing-Dataset.zip' in f:
                zipref = zipfile.ZipFile(f, 'r')
                zipref.extractall('/'.join(f.split('/')[:-1]))
                zipref.close()
        
        self._update_files_list()
               
        # Get dataframe
        for f in self.files:
            if 'day.csv' in f:
                df = pd.read_csv(f)
        df = df.drop('instant', 1)
        df = df.drop('dteday', 1)
        self.dataframe = df
        
