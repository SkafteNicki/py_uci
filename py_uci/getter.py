# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:00:23 2019

@author: nsde
"""
#%%
from .utility import get_uci_table as _get_uci_table
_datasets = _get_uci_table()
from .base import Dataset
from . import formatters as F

#%%
def get(name):
    if name in _datasets['Name'].values:
        return Dataset(name)
    else:
        raise ValueError('Could not find the requested dataset. Check if it is'
                         'in the py_uci.datasets table')

#%%
def datasets_with_formatter():
    datasets = [ ]
    formatted_datasets = dir(F)
    for idx, ds in enumerate(_datasets['Name']):
        if ds.replace(' ','_') in formatted_datasets:
            datasets.append(idx)
    return _datasets.iloc[datasets]        

##%%
#from . import datasets as D
#
##%%
#def get_all():
#    datasets = [ ]
#    for _, d in T.iterrows():
#        datasets.append(eval('D.'+str(d['Name']))())
#    return datasets
#
##%%
#def get_by_filter(task=None, size_min = 0, size_max = 1e20):
#    task = T['Task'].unique() if task == None else task
#    datasets = [ ]
#    for _, d in T.iterrows():
#        if (d['Task'] in task) and (size_min < d['Size'] < size_max):
#            datasets.append(eval('D.'+str(d['Name']))())
#    return datasets
# 
##%% 
#def get(*names):
#    if len(names) == 1:
#        return eval('D.'+str(names[0]))()
#    else:
#        datasets = [ ]
#        for n in names:
#            datasets.append(eval('D.'+str(n))())
#        return datasets