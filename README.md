# Table2XSV
Convert Tabular Data to XSV [CSV, TSV, PSV and Others]

**Python 3.7 <= 3.X <= 3.9**

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

Caution: ```Not a tried and tested method but known to work. If mysql-devel thing does not work replace mysqlclient package with pymysql package in the requirements.txt, setup.cfg, tox.ini and the mysql.py file.```

## Windows
Download, MS VS C++ Redistributable: [Microsoft Visual Studio C++ Redistributable]

Download, Python 3.X: [Python 3.X]

Note (Python): Replace X with Python Minor Version

## Requirements [Build]
```bash
pip install toml tox pluggy
```

## Requirements [Development]
```bash
pip install toml tox pluggy
pip install -r requirements.txt
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
