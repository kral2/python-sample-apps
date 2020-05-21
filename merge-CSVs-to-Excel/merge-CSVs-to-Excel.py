from os import listdir # needed to filter files with a specific extension inside a folder
import pandas as pd # needed to import and export excel files
import re # needed to work with regex

working_dir = './files/20191129'
file_extension = '.csv'
regex_pattern= re.compile(r'([a-z]*)_([a-z_]*).csv', re.IGNORECASE)
output_merged_xslx = 'my_oci_export.xlsx'

def find_files_with_extension(working_dir, file_extension):
   filenames = listdir(working_dir)
   return [ filename for filename in filenames if filename.endswith( file_extension ) ]

def list_filtered_files():
   filtered_files_list = find_files_with_extension(working_dir, file_extension)
   print(f'List of {file_extension} found in {working_dir} directory:')
   i = 0
   for file in filtered_files_list:
       i = i + 1
       print(f'- {file}')
   print(f'Total: {i} {file_extension} files\n')

def merge_csv_files_to_xlsx(regex):
    csv_list = find_files_with_extension(working_dir, file_extension)
    writer = pd.ExcelWriter(output_merged_xslx, engine='xlsxwriter')
    print(f'Starting CSV files merge to {output_merged_xslx}:')
    i = 0
    for file in csv_list:
        current_csv = working_dir + '/' + csv_list[i]
        worksheet_name = re.search(regex, f'{csv_list[i]}') # regex to cut anything before the first underscore and supress file extension
        worksheet_name = worksheet_name.group(2)[:31] # set the worksheet name & truncate if longer than 31 chars
        print(f'import {current_csv} to worksheet: {worksheet_name}')
        current_csv_dataframe = pd.read_csv(current_csv)
        current_csv_dataframe.to_excel(writer, index=None, header=True, sheet_name=worksheet_name)
        i = i +1
    workbook  = writer.book # not used at the moment. Needed to expose the pandas data frame to xlsxwriter and execute additionnal manipulations.
    writer.save()
    writer.close()
    print(f'{output_merged_xslx} generated. It contains {i} worksheets (one per imported csv file).')

def main():
    list_filtered_files()
    merge_csv_files_to_xlsx(regex_pattern)

if __name__ == "__main__":
   main()
