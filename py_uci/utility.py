# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:47:02 2019

@author: nsde
"""

#%%
import os, requests
import numpy as np
from .dataset_table import T

#%%
def get_path(file):
    """ Get the path of the input file """
    return os.path.realpath(file)

#%%
def get_dir(file):
    """ Get directory of the input file """
    return os.path.dirname(os.path.realpath(file))

#%%
def create_dir(direc):
    """ Create a dir if it does not already exists """
    if not os.path.exists(direc):
        os.mkdir(direc)

#%%
def check_if_file_exist(file):
    return os.path.isfile(file)

#%%
def download_file(url,directory):
    """
    Downloads a file from a given url into the given directory.
    """
    local_filename = directory+'/'+url.split('/')[-1]
    if not check_if_file_exist(local_filename):
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        try:
            print('Downloading file: ', url)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024): 
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
        except:
            print("Sorry could not write this particular file:")
            print(url)
    return local_filename
            
#%% 
def convert_to_numeric(str_target, labels):
    num_target = np.zeros_like(str_target)
    for i, l in enumerate(labels):
        num_target[np.where(str_target==l)] = i
    return num_target

#%%
def print_datasets():
    print(T)