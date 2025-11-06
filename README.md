Processes/filters data from Cities.csv

File structure:

oop_lab_1/

|-- README.md            # This file

|-- Cities.csv           # The dataset

|-- data_processing.py   # The analysis code

DataLoader loads data from Cities.csv in the same directory as the Python file.

Table initialises with a name and table data, and creates public attributes with their respective names.
The function filter calls _filter, which takes the table and condition, and returns a new Table with the filtered elements.
The function aggregate calls _aggregate with the table, condition, and aggregation key. Returns the aggregated data.

Testing can be done my modifying Cities.csv and running data_processing.py directly.
Ensure that both files are in the same directory.
