# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:00:23 2019

@author: nsde
"""
#%%
from . import datasets as D
from .dataset_table import T

#%%
def get_all():
    datasets = [ ]
    for _, d in T.iterrows():
        datasets.append(eval('D.'+str(d['Name']))())
    return datasets

#%%
def get_by_filter(task=None, size_min = 0, size_max = 1e20):
    task = T['Task'].unique() if task == None else task
    datasets = [ ]
    for _, d in T.iterrows():
        if (d['Task'] in task) and (size_min < d['Size'] < size_max):
            datasets.append(eval('D.'+str(d['Name']))())
    return datasets
 
#%% 
def get(*names):
    if len(names) == 1:
        return eval('D.'+str(names[0]))()
    else:
        datasets = [ ]
        for n in names:
            datasets.append(eval('D.'+str(n))())
        return datasets