# Table2XSV
Convert Tabular Data to XSV


## Requirements
1. pip install pandas
2. pip install xlrd
3. pip install mysqlclient
4. pip install sqlalchemy
5. pip install pyinstaller

## Complie
pyinstaller --onefile src/Table2XSV.py

### CSV
./Table2XSV csv file.csv

### Excel
./Table2XSV excel file.xlsx SheetName

### SQLite
./Table2XSV sqlite file.db "Query"

### MySQL
./Table2XSV mysql host port user password db "query"

## Optional Arguments
Specify Output File Name: --outfile or -o
Specify Seperator: --sep or -s
Specify Encoding: --encoding or -e
