# Table2XSV
Convert Tabular Data to XSV

## Requirements
    pip install pandas
    pip install xlrd
    pip install mysqlclient
    pip install neo4j
    pip install sqlalchemy
    pip install pyinstaller

## Compile
pyinstaller --onefile Table2XSV.py --hidden-import='neobolt.packstream.packer' --hidden-import='neobolt.packstream.unpacker' --hidden-import='neobolt.bolt' --hidden-import='neobolt.bolt.io'

### CSV
./Table2XSV csv file.csv
### Excel
./Table2XSV excel file.xlsx SheetName
### MySQL
./Table2XSV mysql host port user password db "Query"
### Neo4j
./Table2XSV neo4j host port user password "Query"
### SQLite
./Table2XSV sqlite file.db "Query"

## Optional Arguments
Specify Output File Name: --outfile or -o

Specify Seperator: --sep or -s

Specify Encoding: --encoding or -e