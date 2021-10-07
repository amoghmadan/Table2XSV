# Table2XSV
Convert Tabular Data to XSV

**Python 3.9 >= 3.X >= 3.7**

## Ubuntu
    apt-get install python3.X-venv python3.X-dev libssl-dev libmysqlclient-dev

## Windows
    Install Visual C++ Redistributable [Latest]

## Requirements [For Build]
    pip install -r requirements/build.txt

## Requirements [For Development]
    pip install -r requirements/build.txt
    pip install -r requirements/development.txt

## Compile
tox -c . -e py{37,38,39,310}-pyinstaller
Find Build Under src/dist/table2xsv

## Help
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
