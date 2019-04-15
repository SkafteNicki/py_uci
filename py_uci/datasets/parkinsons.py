# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:46:24 2019

@author: nsde
"""


#%%
import pandas as pd
import numpy as np
from ..base import Dataset
from ..utility import convert_to_numeric

#%%
class parkinsons(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'parkinsons_updrs.data' in f:
                df = pd.read_csv(f, sep=',', header=None)
        self.dataframe = df