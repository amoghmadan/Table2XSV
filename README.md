# Table2XSV
Convert Tabular Data to XSV [CSV, TSV, PSV, etc.]

**Python 3.9 >= 3.X >= 3.7**

## Ubuntu
    sudo apt-get install python3.X-venv python3.X-dev libssl-dev libmysqlclient-dev

Note: Replace X with Python Minor Version

## Windows
Download, MS VS C++ Redistributable: [Microsoft Visual Studio C++ Redistributable]

Download, Python 3.X: [Python 3.X]

Note: Replace X with Python Minor Version

## Requirements [For Build]
    pip install tox pluggy

## Requirements [For Development]
    pip install tox pluggy
    pip install -r requirements.txt

## Compile
    tox -c src -e py3X-pyinstaller

Find Dist Under src/dist/Table2XSV-py3X

Note: Replace X with Python Minor Version

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

[Microsoft Visual Studio C++ Redistributable]: https://www.microsoft.com/en-in/download/details.aspx?id=48145
[Python 3.X]: https://www.python.org/downloads/windows/
