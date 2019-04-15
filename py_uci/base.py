# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:55:27 2019

@author: nsde
"""
#%%
from bs4 import BeautifulSoup
import requests
import os
import numpy as np
import pandas as pd

from .dataset_table import T
from .utility import get_dir, download_file, check_if_file_exist, convert_to_numeric

#%%
class Dataset(object):
    def __init__(self, debug=True):
        # Set class properties based on data table
        self.name, self.size, self.features, self.task, self.weblink = \
            T.unpack(self.__class__.__name__)
        self.loc = get_dir(__file__) + '/../downloaded_datasets/' + \
                   self.weblink.split('/')[-2].replace('-','_')
        
        # Initialize some structures
        self.files = [ ]
        
        # Download files
        self._downloader()
        
        # Read files and format dataframe
        if not check_if_file_exist(self.loc + '/processed_' + self.name + '.pkl'):
            self._create_dataframe()
            if not debug: self._save_dataframe()
        else:
            if not debug: self._load_dataframe()
                
    def _downloader(self):
        # Create directory for files
        if not os.path.exists(self.loc):
            os.makedirs(self.loc)

        # Scrape through webpage
        r = requests.get(self.weblink)
        data = r.text
        soup = BeautifulSoup(data,'html5lib')        
        
        # Download all files
        for i, link in enumerate(soup.find_all('a')):
            if i >= 1: # first is always link to parent directory
                filepage = self.weblink + link.get('href')
                filename = download_file(filepage, self.loc)
                self.files.append(filename)
    
    def _save_dataframe(self):
        self.dataframe.to_pickle(self.loc + '/processed_' + self.name + '.pkl')
        
    def _load_dataframe(self):
        self.dataframe = pd.read_pickle(self.loc + '/processed_' + self.name + '.pkl')
    
    def _update_files_list(self):
        self.files = [ ]
        for f in os.listdir(self.loc):
            self.files.append(self.loc + '/' + f)
    
    @property
    def N(self):
        return self.data.shape[0]
    
    @property
    def d(self):
        return self.data.shape[1]
    
    @property
    def data(self):
        return self.dataframe.values[:,:-1].astype('float32')
    
    @property
    def target(self):
        return convert_to_numeric(self.dataframe.values[:,-1])
    
    @property
    def attribute_names(self):
        return list(self.dataframe)
    
    def _create_dataframe():
        raise NotImplementedError
        
        
        
    