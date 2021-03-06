# py_uci

Python library for loading data from the UCI Machine Learning Repository. I
created this repository since I needed to test out some algorithms on multiple
datasets and could not find a simple python API that can be used to download
a bunch of datasets. Therefore I created this small repo. 

## Install

Simply clone the repo and install with `python setup.py install`. The repo
depends mostly on numpy, pandas and other build in library. If you are running
python through anaconda, you should be good to go.

## How to use

The library can simply be imported by
```
    import py_uci
```
Then to fetch some datasets you can use the following methods
```
    # get a single dataset characterize by its name
    dataset = py_uci.get('name') 
    
    # get multiple datasets (returned as a list) by giving the name of each
    datasets = py_uci.get('name1', 'name2', ...)
    
    # get multiple datasets either by a specific taks ('classification', 'regression')
    # or the number of sample in the dataset
    datasets = py_uci.get_by_filter(task='task', 
                                    min_size=lower_size,
                                    max_size=upper_size)
    
    # get all datasets
    datasets = py_uci.get_all()
    
```

Each dataset come with a number of attributes, where the most important is the
`dataset.dataframe`. This is a `pandas.DataFrame` with all the extracted
information about the dataset. For easy to use, the following is also availble:

```
    dataset.N # number of samples
    dataset.d # number of features
    dataset.data # returns numeric numpy array with the input features of the dataset
    dataset.target # returns numeric vector with the target values for the dataset
```

## How to extend
I have basically only included the datasets that I used myself. That said, you
can easily add your own datasets to the mix.

Add a row with the name, size, type and weblink of the dataset to the `py_uci.dataset_table.py`
file and secondly create a file in the datasets folder, where you implement the
correponding class. This basically amounts to implementing the `._create_dataframe(self)`
method for the class. In most cases everything else is taken care of the base class.
If this does not work, simply check out some of the other datasets on how to format
the `.data` and `.target` attribute. Lastly add the newly implemented class in the
`datasets/__init__.py` file.

Feel free to send me a pull request with your implemented dataset.