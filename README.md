# Table2XSV
Convert Tabular Data to XSV [CSV, TSV, PSV and Others]

**Python 3.9 >= 3.X >= 3.7**

## Debian [Ubuntu, Mint and Others]
    sudo apt-get install python3.X-venv python3.X-dev libssl-dev libmysqlclient-dev build-essential
Note: Replace X with Python Minor Version

## Redhat [CentOS, Rocky, Fedora and Others]
    sudo yum/dnf install python3.X python3.X-devel ssl-devel mysql-devel
Note: Replace X with Python Minor Version

Caution: ```Not a tried and tested method but known to work. If mysql-devel thing does not work replace mysqlclient package with pymysql package in the requirements.txt, setup.cfg, tox.ini and the mysql.py file.```

## Windows
Download, MS VS C++ Redistributable: [Microsoft Visual Studio C++ Redistributable]

Download, Python 3.X: [Python 3.X]

Note: Replace X with Python Minor Version

## Requirements [Build]
    pip install toml tox pluggy

## Requirements [Development]
    pip install toml tox pluggy
    pip install -r requirements.txt

## Generate [Build (Distribution and Wheel)]
    tox -c . -e py3X-buid

Note: Replace X with Python Minor Version

## Install [Wheel]
    cd dist
    pip install Table2XSV-{version}-py3X-none-any.whl

Note: Replace X with Python Minor Version

# Generate [Executable]
    tox -c . -e py3X-build-exe  # All Optionals Will Be Installed

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
