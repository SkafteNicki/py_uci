# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:38:27 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset
import zipfile

#%%
class year_prediction(Dataset):
    def _create_dataframe(self):
        # Extract .zip file
        for f in self.files:
            if 'YearPredictionMSD.txt.zip' in f:
                zipref = zipfile.ZipFile(f, 'r')
                zipref.extractall('/'.join(f.split('/')[:-1]))
                zipref.close()
        
        self._update_files_list()
               
        # Get dataframe
        for f in self.files:
            if 'YearPredictionMSD.txt' in f:
                df = pd.read_csv(f, header=None)
        self.dataframe = df
        
    @property
    def data(self):
        return self.dataframe.values[:,1:].astype('float32')
    
    @property
    def target(self):
        return self.dataframe.values[:,0].astype('float32')
    
    
