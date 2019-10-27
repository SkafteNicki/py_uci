# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:58:16 2019

@author: nsde
"""

#%%
from setuptools import setup

#%%
setup(name = "py_uci",
      version = "0.1",
      description = "Python library for easy loading and working with multiple"
                    "datasets from the UCI Machine Learning Reposatory",
      author = "Nicki Skafte Detlefsen",
      author_email = "nsde@dtu.dk",
      packages = ["py_uci", "py_uci.datasets"],
      license = "MIT",
      long_description = open('README.md').read())
