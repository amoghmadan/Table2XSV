# Table2XSV
Convert Tabular Data to XSV [CSV, TSV, PSV and Others]

**Python 3.8 <= 3.X < 3.13**

**Setup CSV and SQLite (Basic Installation)**
```bash
pip install table2xsv  # Setup CSV and SQLite by Default
```

**Setup (All Installation)**
```bash
pip install table2xsv[all]  # Setup All
```

## Debian [Ubuntu, Mint and Others]
```bash
sudo apt-get install python3.X-venv python3.X-dev libssl-dev libmysqlclient-dev build-essential
```
Note (Python): Replace X with Python Minor Version

## Redhat [CentOS, Rocky, Fedora and Others]
```bash
sudo yum install python3.X python3.X-devel ssl-devel mysql-devel
```
Note (Python): Replace X with Python Minor Version

Note (Fedora): Replace yum with dnf

## Windows
Download, MS VS C++ Redistributable: [Microsoft Visual Studio C++ Redistributable]

Download, Python 3.X: [Python 3.X]

Note (Python): Replace X with Python Minor Version

## Requirements [Build]
```bash
pip install tox
```

## Requirements [Development]
```bash
pip install -e .[all]
pip install -e .[development]
```

## Generate [Build (Distribution and Wheel)]
```bash
tox -c . -e py3X-build
```

Note: Replace X with Python Minor Version

## Install [Wheel]
```bash
cd dist
pip install Table2XSV-{version}-py3X-none-any.whl[all]  # All Optionals Will Be Installed
```
Note: Replace X with Python Minor Version

# Generate [Executable]
```bash
tox -c . -e py3X-build-exe  # All Optionals Will Be Installed
```
Caution: _Works a bit slower._ Remove the -F flag in tox.ini and use the build folder path to make it faster.

Note (Python): Replace X with Python Minor Version

## Help
```bash
Table2XSV -h
```

### CSV
```bash
Table2XSV csv -h
```

### Excel
```bash
Table2XSV excel -h
```

### MySQL
```bash
Table2XSV mysql -h
```

### Neo4j
```bash
Table2XSV neo4j -h
```

### SQLite
```bash
Table2XSV sqlite -h
```

[Microsoft Visual Studio C++ Redistributable]: https://www.microsoft.com/en-in/download/details.aspx?id=48145
[Python 3.X]: https://www.python.org/downloads/windows/
