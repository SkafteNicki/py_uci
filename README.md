# py_uci
Python library for loading data from the UCI Machine Learning Repository

## How to use


## How to extend
I have basically only included the datasets that I used myself. That said, you
can easily add your own datasets to the mix.

Add a row with the name, size, type and weblink of the dataset to the `py_uci.dataset_table.py`
file and secondly create a file in the datasets folder, where you implement the
correponding class. Then finally you can run the `test.py` file to check that the
class extracts all nessesary information.

## Dependencies

* Pandas
* Numpy
