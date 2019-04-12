# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:55:27 2019

@author: nsde
"""
#%%
from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import numpy as np
import pandas as pd

from .utility import get_dir, download_file, check_if_file_exist, get_uci_table
_datasets = get_uci_table()
from . import formatters as F

#%%
class Dataset(object):
    def __init__(self, name):
        # Initialize from table
        self.name, self.dtype, self.task, self.att_type, self.instances, \
            self.attributes, self.year = _datasets[_datasets['Name']==name].values[0]
        self.name = self.name.replace(' ','_')
        self.instances = int(self.instances)
        self.attributes = int(self.attributes)
        self.year = int(self.year)
        self.files = [ ]
        
        # Get download link
        self.weblink = self._get_download_link()
        self.loc = get_dir(__file__) + '/../downloaded_datasets/' + \
                   self.weblink.split('/')[-2].replace('-','_')
                   
        # Download all files
        self._downloader()
        
        # Extrac dataframe
        if not check_if_file_exist(self.loc + '/processed_' + self.name + '.pkl'):
            self.dataframe = self._create_dataframe()
            self._save_dataframe()
        else:
            self._load_dataframe()
    
    def _get_download_link(self):
        base_url = 'https://archive.ics.uci.edu/ml/datasets.php'
        url = base_url[:-4] + '/' + self.name.replace('_','+')
        
        uh= urllib.request.urlopen(url)
        html =uh.read()
        
        soup = BeautifulSoup(html, features="lxml")
        return base_url[:-4] + '/' + soup.find_all('a')[8].get('href')
    
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

    def _create_dataframe(self):
        if self.name in dir(F):
            return eval('F.' + self.name)(self)
        else:
            raise ValueError('No formatter known for this dataset')
            
    def _update_file_list(self):
        self.files = [ ]
        for f in os.listdir(self.loc):
            self.files.append(self.loc + '/' + f)
        
        
    