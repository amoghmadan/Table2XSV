# Table2XSV
Convert Tabular Data to XSV

## Ubuntu
    apt-get install python3.7-dev libssl-dev libmysqlclient-dev

## Windows
    Install Visual C++ Redistributable [Latest]

## Requirements
    pip install pandas xlrd sqlalchemy mysqlclient neo4j pyinstaller

## Compile
pyinstaller --onefile src/Table2XSV.py --hidden-import='neobolt.packstream.packer' --hidden-import='neobolt.packstream.unpacker' --hidden-import='neobolt.bolt' --hidden-import='neobolt.bolt.io'

## Help
Table2XSV -h

### CSV
Table2XSV csv -h

### Excel
Table2XSV excel -h

### SQLite
Table2XSV sqlite -h

### MySQL
Table2XSV mysql -h

### Neo4j
Table2XSV neo4j -h
