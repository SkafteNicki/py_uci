# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:07:52 2019

@author: nsde
"""

#%%
import pandas as pd
from .base import Dataset

#%%
class yacht_hydrodynamics(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'yacht_hydrodynamics.data' in f:
                df = pd.read_csv(f, header=None, delim_whitespace=True)
        self.dataframe = df
        self.dataframe.columns = ['Longitudinal position of the center of buoyancy, adimensional.',
                                  'Prismatic coefficient, adimensional.',
                                  'Length-displacement ratio, adimensional.',
                                  'Beam-draught ratio, adimensional.',
                                  'Length-beam ratio, adimensional.',
                                  'Froude number, adimensional. ']