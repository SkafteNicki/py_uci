# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:11:42 2019

@author: nsde
"""

#%%
import pandas as pd

#%%
class mydataframe(pd.DataFrame):
    _append_counter = 0
    
    def row_append(self, row):
        self.loc[self._append_counter] = row
        self._append_counter += 1
        
    def unpack(self, name):
        return self[self['Name'] == name].values[0]

#%%
T = mydataframe(columns = ['Name', 'Size', 'Task', 'weblink'])
T.row_append(['iris', 150, 'classification', 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'])
T.row_append(['wine_quality', 6497, 'classification', 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'])
T.row_append(['wine_red', 4898, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'])
T.row_append(['wine_white', 1599, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'])
T.row_append(['boston', 506, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/'])
T.row_append(['power_plant', 9568, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/00294/'])
T.row_append(['carbon_nanotubes', 10721, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/00448/'])
T.row_append(['forest_fire', 517, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/'])
T.row_append(['concrete', 1030, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/compressive/'])
T.row_append(['superconduct', 21263, 'regression', 'https://archive.ics.uci.edu/ml/machine-learning-databases/00464/'])