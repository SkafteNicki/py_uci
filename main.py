# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:58:36 2019

@author: nsde
"""

#%%
#from uci_regression import downloaders as D
#from uci_regression import get_dataset

import py_uci
datasets = py_uci.get_all()


#d = D.iris()

##%%
#def get_dir(file):
#    """ Get directory of the input file """
#    import os
#    return os.path.dirname(os.path.realpath(file))
#
#
##%%
#from bs4 import BeautifulSoup
#import requests
#import os
#dataset = 'iris'
#weblink = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'
##weblink = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'
#
#d = get_dir(__file__)
#loc = d + '/datasets/' + dataset
#if not os.path.exists(loc):
#    os.makedirs(loc)
#
#r = requests.get(weblink)
#data = r.text
#soup = BeautifulSoup(data,'html5lib')
#
#
#
#for i, link in enumerate(soup.find_all('a')):
#    if i > 4:
#        filepage = weblink + link.get('href')
#        download_file(filepage, loc)
#        
#            
##        a=link.attrs['href']
##        a=a[2:]
##        dataurl="https://archive.ics.uci.edu/ml/"+str(a)
##        print(dataurl)


