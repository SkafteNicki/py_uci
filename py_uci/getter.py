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
    ''' Get all datasets in the database '''
    datasets = [ ]
    for _, d in T.iterrows():
        datasets.append(eval('D.'+str(d['Name']))())
    return datasets

#%%
def get_by_filter(task=None, 
                  size_min = 0, 
                  size_max = 1e20, 
                  features_min = 0,
                  features_max = 1e20):
    ''' Get all datasets that forfill specific criteria
    Arguments:
        task: string, dataset task {'regression', 'classification'}
        size_min: int, minimum number of observations in dataset
        size_max: int, maximum number of observations in dataset
        features_min: int, minimum number of features in dataset
        features_max: int, maximum number of features in dataset
    '''
    task = T['Task'].unique() if task == None else task
    datasets = [ ]
    for _, d in T.iterrows():
        if      (d['Task'] in task) and \
                (size_min < d['Size'] < size_max) and \
                (features_min < d['Features'] < features_max):
            datasets.append(eval('D.'+str(d['Name']))())
    return datasets
 
#%% 
def get(*names):
    ''' Get a single or a number of datasets specified by their names '''
    if len(names) == 1:
        return eval('D.'+str(names[0]))()
    else:
        datasets = [ ]
        for n in names:
            datasets.append(eval('D.'+str(n))())
        return datasets