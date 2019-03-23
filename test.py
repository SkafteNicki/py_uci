# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:58:09 2019

@author: nsde
"""

#%%
import unittest
import py_uci

#%%
class TestDatasets(unittest.TestCase):
    
    datasets = py_uci.get_all()
    
    def test_has_data_attr(self):
        for d in self.datasets:
            testbool = hasattr(d, 'data')
            self.assertTrue(testbool, msg="obj lacking an attribute. "
                "obj: %s, intendedAttr: %s".format(d, 'data'))
            
    
    def test_has_dataframe_attr(self):
        for d in self.datasets:
            testbool = hasattr(d, 'dataframe')
            self.assertTrue(testbool, msg="obj lacking an attribute. "
                "obj: %s, intendedAttr: %s".format(d, 'dataframe'))
    
    
    def test_has_target_attr(self):
        for d in self.datasets:
            testbool = hasattr(d, 'target')
            self.assertTrue(testbool, msg="obj lacking an attribute. "
                "obj: %s, intendedAttr: %s".format(d, 'target'))
    
#%%
if __name__ == '__main__':
    unittest.main()