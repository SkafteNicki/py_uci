# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:00:23 2019

@author: nsde
"""
#%%
from . import datasets as D

#%%
def get_all():
    datasets = [ ]
    for d in D.VALID_DATASETS:
        datasets.append(eval('D.'+str(d))())
    return datasets

#%%
def get_by_task(task):
    datasets = [ ]
    for d, t in D.BY_TASK.items():
        if t == task:
            datasets.append(eval('D.'+str(d))())
    return datasets

#%%
def get_by_size(size_min = 0, size_max = 1e20):
    datasets = [ ]
    for d, s in D.BY_SIZE.items():
        if size_min < d < size_max:
            datasets.append(eval('D.'+str(d))())
    return datasets
 
#%% 
def get(name):
    return eval('D.'+str(name))()