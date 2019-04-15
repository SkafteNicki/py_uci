# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 07:52:22 2019

@author: nsde
"""

#%%
import pandas as pd
from ..base import Dataset
import zipfile, os

#%%
class naval(Dataset):
    def _create_dataframe(self):
        # Extract .zip file
        for f in self.files:
            if 'UCI%20CBM%20Dataset.zip' in f:
                zipref = zipfile.ZipFile(f, 'r')
                zipref.extractall('/'.join(f.split('/')[:-1]))
                zipref.close()
        
        self._update_files_list()
             
        # Move files from folder to data folder
        for f in self.files:
            if os.path.isdir(f) and '_MACOSX' not in f:
                for ff in os.listdir(f):
                    old = f + '/' + ff
                    new = '/'.join(f.split('/')[:-1]) + '/' + ff.split('/')[-1]
                    os.rename(old, new)

        self._update_files_list()
        
        # Get dataframe
        for f in self.files:
            if 'data.txt' in f:
                df = pd.read_fwf(f, header=None)
        self.dataframe = df
        self.dataframe.columns = ['Lever position', 'Speed', 'GTT',
            'GTn', 'GGn', 'Ts', 'Tp', 'T48', 'T1', 'T2', 'P48', 'P1', 
            'P2', 'Pexh', 'TIC', 'mf', 'Comp. decay', 'Turb. decay ']
