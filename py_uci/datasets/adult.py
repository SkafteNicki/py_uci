# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:59:03 2019

@author: nsde
"""


#%%
import pandas as pd
from ..base import Dataset

#%%
class adult(Dataset):
    def _create_dataframe(self):
        for f in self.files:
            if 'adult.data' in f:
                df1 = pd.read_csv(f, sep=',', header=None)
            if 'adult.test' in f:
                df2 = pd.read_csv(f, sep=',', header=None, skiprows=1)
        df = pd.concat([df1, df2], axis=0, ignore_index=True)
        df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                      'marital-status', 'occupation', 'relationship', 'race',
                      'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                      'income']
        df['income'] = df['income'].replace(' <=50K.', '<=50K')
        df['income'] = df['income'].replace(' >50K.', '>50K')
        self.dataframe = df
        