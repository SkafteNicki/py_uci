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
    def _formatter(self):
        for f in self.files:
            if 'iris.data' in f:
                df = pd.read_csv(f, header=None)
        self.dataframe = df
        self.data = df.values[:,:-1].astype('float32')
        self.attribute_name = ['sepal length', 'sepal width', 
                               'petal length', 'petal width']
        self.labels = np.unique(df.values[:,-1])
        self.target = convert_to_numeric(df.values[:,-1], self.labels).astype('int32')