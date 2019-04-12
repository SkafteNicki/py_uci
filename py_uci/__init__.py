# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:53:50 2019

@author: nsde
"""

#%%
from .getter import get, datasets_with_formatter
from . import utility
from .utility import get_uci_table as _get_uci_table
datasets = _get_uci_table()

