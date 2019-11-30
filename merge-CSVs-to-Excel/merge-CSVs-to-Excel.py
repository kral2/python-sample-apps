from os import listdir
import pandas as pd

working_dir = './files/20191129'
file_extension = '.csv'
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

def merge_csv_files_to_xlsx():
    csv_list = find_files_with_extension(working_dir, file_extension)
    writer = pd.ExcelWriter(output_merged_xslx, engine='xlsxwriter')
    print(f'Starting CSV files merge to {output_merged_xslx}:')
    i = 0
    for file in csv_list:
        current_csv = working_dir + '/' + csv_list[i]
        print(f'import {current_csv}')
        current_csv_dataframe = pd.read_csv(current_csv)
        current_csv_dataframe.to_excel(writer, index=None, header=True, sheet_name=f'{csv_list[i]}')
        i = i +1
    workbook  = writer.book
    writer.save()
    writer.close()
    print(f'{output_merged_xslx} generated. It contains {i} worksheets (one per imported csv file).')

def main():
    list_filtered_files()
    merge_csv_files_to_xlsx()

if __name__ == "__main__":
   main()