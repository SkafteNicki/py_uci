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
T = mydataframe(columns = ['Name', 'Size', 'Features', 'Task', 'weblink'])
T.row_append(['iris',               150,    4,  'classification',   'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'])
T.row_append(['wine_quality',       6497,   12, 'classification',   'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'])
T.row_append(['wine_red',           4898,   11, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'])
T.row_append(['wine_white',         1599,   11, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'])
T.row_append(['boston',             506,    13, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/'])
T.row_append(['power_plant',        9568,   3,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00294/'])
T.row_append(['carbon_nanotubes',   10721,  7,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00448/'])
T.row_append(['forest_fire',        517,    13, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/'])
T.row_append(['concrete',           1030,   9,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/compressive/'])
T.row_append(['superconduct',       21263,  81, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00464/'])
T.row_append(['bike_sharing',       17389,  16, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00275/'])
T.row_append(['naval',              11934,  16, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00316/'])
T.row_append(['yacht_hydrodynamics',308,    7,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00243/'])
T.row_append(['auto_mpg',           398,    8,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/'])
T.row_append(['abalone',            4177,   8,  'classification',   'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/'])
# Checked
T.row_append(['protein_structure',  45730,  9,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00265/'])
T.row_append(['adult',              48842,  14, 'classification',   'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/'])
T.row_append(['year_prediction',    515345, 90, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00203/'])
T.row_append(['blood_pressure',     12000,  3,  'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/00340/'])
T.row_append(['parkinsons',         5875,   26, 'regression',       'https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/telemonitoring/'])



