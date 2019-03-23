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

from ..dataset_table import T
from ..utility import get_dir, download_file

#%%
class Dataset(object):
    def __init__(self):
        # Set class properties based on data table
        self.name, self.size, self.task, self.weblink = \
            T.unpack(self.__class__.__name__)
        
        # Initialize some structures
        self.files = [ ]
        
        # Download files
        self._downloader()
        
        # Read files and format into arrays
        self._formatter()
        
    def _downloader(self):
        # Create directory for files
        d = get_dir(__file__)
        loc = d + '/../../downloaded_datasets/' + \
              self.weblink.split('/')[-2].replace('-','_')
        if not os.path.exists(loc):
            os.makedirs(loc)

        # Scrape through webpage
        r = requests.get(self.weblink)
        data = r.text
        soup = BeautifulSoup(data,'html5lib')        
        
        # Download all files
        for i, link in enumerate(soup.find_all('a')):
            if i > 4:
                filepage = self.weblink + link.get('href')
                filename = download_file(filepage, loc)
                self.files.append(filename)
    
    def test_train_split(self, test_size, seed=None):
        seed = seed if seed is not None else np.random.randint(0,1e6)
        np.random.seed(seed)
        idx = np.random.permutation(self.N)
        test_size = int(np.round(self.N*test_size))
        test = idx[:test_size]
        train = idx[test_size:]
        return train, test
    
    def cv_split(self, K=2, holdout_size = 0.1, seed=None):
        seed = seed if seed is not None else np.random.randint(0,1e6)
        np.random.seed(seed)
        idx = np.random.permutation(self.N)
        holdout_size = int(np.round(self.N*holdout_size))
        cv_size = int(np.round((self.N - holdout_size)/K))
        holdout = idx[:holdout_size]
        remaining = idx[holdout_size:]
        remaining = [remaining[k*cv_size:(k+1)*cv_size] for k in range(K)]
        cvs_train = [ ]
        cvs_val = [ ]
        for k in range(K):
            cvs_train.append(np.concatenate(
                [remaining[kk] for kk in range(K) if kk != k], axis=0))
            cvs_val.append(remaining[k])
        return cvs_train, cvs_val, holdout
        
    @property
    def N(self):
        return self.data.shape[0]
    
    @property
    def d(self):
        return self.data.shape[1]
        
    def _formatter():
        raise NotImplementedError
        
        
        
    