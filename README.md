# Table2XSV
Convert Tabular Data to XSV

## Ubuntu
    apt install python[VERSION IF ANY]-dev libssl-dev libmysqlclient-dev

## Requirements
    pip install pandas xlrd sqlalchemy mysqlclient neo4j pyinstaller

## Compile
pyinstaller --onefile src/Table2XSV.py --hidden-import='neobolt.packstream.packer' --hidden-import='neobolt.packstream.unpacker' --hidden-import='neobolt.bolt' --hidden-import='neobolt.bolt.io'

## Run
### CSV
Table2XSV csv --path=file.csv

### Excel
Table2XSV excel --path=<FILE_PATH>.xlsx --sheet=<SHEET_NAME>

### SQLite
Table2XSV sqlite --path=<FILE_PATH>.db --query=<QUERY_HERE>

### MySQL
Table2XSV mysql --host=<DEFAULT: LOCALHOST> --port=<DEFAULT_PORT> --user=<USER_HERE> --db=<DB_HERE> --query=<QUERY_HERE>

### Neo4j
Table2XSV neo4j --host=<DEFAULT: LOCALHOST> --port=<DEFAULT_PORT> --user=<USER_HERE> --query=<QUERY_HERE>

## Optional Arguments
Specify Output File Name: --outfile or -o [Default: output current_date_time.csv]

Specify Separator: --sep or -s [Default: ,]

Specify Encoding: --encoding or -e [Default: utf-8]
