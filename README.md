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
pyinstaller --onefile src/Table2XSV.py --hidden-import='neobolt.packstream.packer' --hidden-import='neobolt.packstream.unpacker' --hidden-import='neobolt.bolt' --hidden-import='neobolt.bolt.io'

## Run
### CSV
Table2XSV --source=csv --path=file.csv

### Excel
Table2XSV --source=excel --path=file.xlsx --sheet=SheetName

### MySQL
Table2XSV --source=mysql --host=127.0.0.1 --port=3306 --user=root --password=toor --db=db_name --query="Query"

### Neo4j
Table2XSV --source=neo4j --host=127.0.0.1 --port=7687 --user=neo4j --password=toor --query="Query"

### SQLite
Table2XSV --source=sqlite --path=file.db --query="Query"

## Optional Arguments
Specify Output File Name: --outfile or -o

Specify Separator: --sep or -s

Specify Encoding: --encoding or -e