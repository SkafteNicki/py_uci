# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:58:36 2019

@author: nsde
"""

#%%
import py_uci
ds = py_uci.get('airfoil')
df = ds.dataframe
data = ds.data
target = ds.target
