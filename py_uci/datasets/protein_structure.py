# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:07:53 2019

@author: nsde
"""

#%%
import pandas as pd
from .base import Dataset

#%%
class protein_structure(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'CASP.csv' in f:
                df = pd.read_csv(f)
        self.dataframe = df
        self.dataframe.columns = ['RMSD-Size of the residue.',
                                  'F1 - Total surface area.',
                                  'F2 - Non polar exposed area.',
                                  'F3 - Fractional area of exposed non polar residue.',
                                  'F4 - Fractional area of exposed non polar part of residue.',
                                  'F5 - Molecular mass weighted exposed area.',
                                  'F6 - Average deviation from standard exposed area of residue.',
                                  'F7 - Euclidian distance.',
                                  'F8 - Secondary structure penalty.',
                                  'F9 - Spacial Distribution constraints (N,K Value).']
        