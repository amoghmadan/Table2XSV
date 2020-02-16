import sys
import argparse
from datetime import datetime
from getpass import getpass
import pandas as pd
import MySQLdb
from neo4j import GraphDatabase
import sqlite3


class Table2XSV(object):
    """Class to convert Table Data to XSV"""

    index = False

    def __str__(self):
        return 'Class to retrieve tabular data from CSV, Excel, SQLite, MySQL, Neo4j to XSV.'

    def __repr__(self):
        return 'Table2XSV(outfile, sep, encoding)'

    def csv2xsv(self, **kwargs):
        if not kwargs['path']:
            print('Error: --path is required with source: csv')
        elif not kwargs['path'].endswith(('.csv', '.tsv', '.psv')):
            print('Error: Invalid file, can only accept files ending with .csv or .tsv or .psv')
        else:
            df = pd.read_csv(kwargs['path'])
            df.to_csv(kwargs['outfile'], index=self.index, sep=kwargs['sep'], encoding=kwargs['encoding'])

    def excel2xsv(self, **kwargs):
        if not kwargs['path'] or not kwargs['sheet']:
            print('Error: --path and --sheet are required with source: excel')
        elif not kwargs['path'].endswith(('.xlsx', '.xls')):
            print('Error: Invalid file, can only accept files ending with .xlsx or .xls')
        else:
            df = pd.read_excel(kwargs['path'], sheet_name=kwargs['sheet'])
            df.to_csv(kwargs['outfile'], index=self.index, sep=kwargs['sep'], encoding=kwargs['encoding'])

    def sqlite2xsv(self, **kwargs):
        if not kwargs['path'] or not kwargs['query']:
            print('Error: --path and --query are required with source: sqlite')
        elif kwargs['path'].endswith('.db'):
            print('Invalid file, can only accept files ending with .db')
        else:
            with sqlite3.connect(kwargs['path']) as connection:
                df = pd.read_sql_query(kwargs['query'], con=connection)
            df.to_csv(kwargs['outfile'], index=self.index, sep=kwargs['sep'], encoding=kwargs['encoding'])

    def mysql2xsv(self, **kwargs):
        if not kwargs['user'] or not kwargs['db'] or not kwargs['query']:
            print('Error: --host, --port, --user, --db and --query are required with source: mysql')
        else:
            password = getpass(prompt='Password: ', stream=None)
            connection = MySQLdb.connect(host=kwargs['host'], port=kwargs['port'], user=kwargs['user'], passwd=password,
                                         db=kwargs['db'])
            df = pd.read_sql(kwargs['query'], con=connection)
            connection.close()
            df.to_csv(kwargs['outfile'], index=self.index, sep=kwargs['sep'], encoding=kwargs['encoding'])

    def neo4j2xsv(self, **kwargs):
        if not kwargs['user'] or not kwargs['query']:
            print('Error: --host, --port, --user and --query are required with source: neo4j')
        else:
            password = getpass(prompt='Password: ', stream=None)
            uri = 'bolt://{}:{}'.format(kwargs['host'], kwargs['port'])
            driver = GraphDatabase.driver(uri, auth=(kwargs['user'], password))
            with driver.session() as session:
                records = session.run(kwargs['query'])
            df = pd.DataFrame([record.values() for record in records], columns=records.keys())
            df.to_csv(kwargs['outfile'], index=self.index, sep=kwargs['sep'], encoding=kwargs['encoding'])


if __name__ == '__main__':
    """."""

    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='provide source type, possible types csv, excel, sqlite, mysql and neo4j')
    parser.add_argument('--path', help='provide file path (csv, excel and sqlite only)')
    parser.add_argument('--sheet', help='provide sheet name (excel only)')
    parser.add_argument('--host', default='127.0.0.1', help='provide host (mysql and neo4j only)')
    parser.add_argument('--port', help='provide port (mysql and neo4j only)', type=int)
    parser.add_argument('--user', help='provide user (mysql and neo4j only)')
    parser.add_argument('--db', help='provide database name (mysql only)')
    parser.add_argument('--query', help='provide query (sqlite, mysql and neo4j only)')
    parser.add_argument('-o', '--outfile', default='output {}.csv'.format(datetime.now()),
                        help='provide name for the output file (with extension as csv)')
    parser.add_argument('-s', '--sep', default=',', help='provide a separator')
    parser.add_argument('-e', '--encoding', default='utf-8', help='provide an encoding')
    args = parser.parse_args()

    default_port: dict = {'mysql': 3306, 'neo4j': 7687}

    try:
        source: str = args.source.strip().lower()

        if not args.port and source in default_port:
            args.port = default_port[source]

        table2xsv: Table2XSV = Table2XSV()

        dispatcher: dict = {
            'csv': table2xsv.csv2xsv,
            'excel': table2xsv.excel2xsv,
            'sqlite': table2xsv.sqlite2xsv,
            'mysql': table2xsv.mysql2xsv,
            'neo4j': table2xsv.neo4j2xsv
        }

        try:
            dispatcher[source](**vars(args))
        except KeyError:
            print('Please refer command line args help module by using --help')

    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print('Class: {} | Error: {} | Line Number: {}'.format(tc, exc, tb.tb_lineno))
