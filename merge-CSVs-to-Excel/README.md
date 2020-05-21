# Merge CSVs to Excel

This script looks for csv files in a directory, and merge them all in a single xlsx file.
It makes use of pandas and XlsxWriter.

## Usage

1. Edit merge-CSVs-to-Excel.py

At the top of the script, initialize your variables as needed :

- the folder where the CSV files are stored,
- the path and file name where to put the merge excel file,
- the regex pattern to match, inside re.compile().

``` python
working_dir = './files/myfolder'
output_merged_xslx = 'myfile.xlsx'
regex_pattern= re.compile(r'([0-9_-a-z]*)_([a-zA-Z_-]*).csv', re.IGNORECASE)
```

2. Get your python environment with the requirements up & running

You will need to install pandas and xlsxwriter: ```pip install pandas xlsxwriter```

3. Run the script

```python merge-CSVs-to-Excel.py```

## Current development status & limitations

Working version, but still need some enhancements:

- Code comments & documentation,
- Tests and error handling,
- Sample data.
