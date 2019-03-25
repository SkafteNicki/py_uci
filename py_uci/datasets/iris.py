#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:31:40 2019

@author: nsde
"""

#%%
import pandas as pd
import numpy as np
from .base import Dataset
from ..utility import convert_to_numeric

#%%
class iris(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'iris.data' in f:
                df = pd.read_csv(f, header=None)
        self.dataframe = df
        self.dataframe.columns = ['sepal length', 'sepal width', 
                                  'petal length', 'petal width', 'flower type']
