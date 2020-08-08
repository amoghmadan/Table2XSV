import sys
import argparse
from getpass import getpass
from datetime import datetime

import sqlite3
import pandas as pd
from MySQLdb import Connection
from neo4j import GraphDatabase


class Table2XSV(object):
    """."""

    index = False

    def __init__(self):
        """."""

        out_file = 'output_{}.csv'.format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

        parser = argparse.ArgumentParser(description='')
        sub_parser = parser.add_subparsers(title='commands', dest='command')

        csv = sub_parser.add_parser('csv', help='Read from XSV write to XSV')
        csv.add_argument('path', type=str, help='Provide path of XSV file')
        csv.add_argument('-o', '--outfile', type=str, default=out_file,
                         help='Provide path to output XSV file, default=output_datetime.csv')
        csv.add_argument('-e', '--encoding', type=str, default='utf-8',
                         help='Provide encoding for output XSV file, default=utf-8')
        csv.add_argument('-s', '--separator', type=str, default=',', help='Provide separator for columns, default=,')

        excel = sub_parser.add_parser('excel', help='Read from Excel Sheet write to XSV')
        excel.add_argument('path', type=str, help='Provide path of Excel file')
        excel.add_argument('-S', '--sheet', type=str, default='Sheet1', help='Provide name of sheet, default=Sheet1')
        excel.add_argument('-o', '--outfile', type=str, default=out_file,
                           help='Provide path to output XSV file, default=output_datetime.csv')
        excel.add_argument('-e', '--encoding', type=str, default='utf-8',
                           help='Provide encoding for output XSV file, default=utf-8')
        excel.add_argument('-s', '--separator', type=str, default=',', help='Provide separator for columns, default=,')

        sqlite = sub_parser.add_parser('sqlite', help='Read from SQLite query write to XSV')
        sqlite.add_argument('path', type=str, help='Provide path of SQLite file')
        sqlite.add_argument('query', type=str, help='Provide query to return tabular data')
        sqlite.add_argument('-o', '--outfile', type=str, default=out_file,
                            help='Provide path to output XSV file, default=output_datetime.csv')
        sqlite.add_argument('-e', '--encoding', type=str, default='utf-8',
                            help='Provide encoding for output XSV file, default=utf-8')
        sqlite.add_argument('-s', '--separator', type=str, default=',', help='Provide separator for columns, default=,')

        mysql = sub_parser.add_parser('mysql', help='Read from MySQL query write to XSV')
        mysql.add_argument('user', type=str, help='MySQL user to connect')
        mysql.add_argument('database', type=str, help='MySQL db to connect')
        mysql.add_argument('query', type=str, help='Provide query to return tabular data')
        mysql.add_argument('-H', '--host', type=str, default='127.0.0.1',
                           help='MySQL host to connect, default=127.0.0.1')
        mysql.add_argument('-p', '--port', type=int, default=3306, help='MySQL port to connect, default=3306')
        mysql.add_argument('-o', '--outfile', type=str, default=out_file,
                           help='Provide path to output XSV file, default=output_datetime.csv')
        mysql.add_argument('-e', '--encoding', type=str, default='utf-8',
                           help='Provide encoding for output XSV file, default=utf-8')
        mysql.add_argument('-s', '--separator', type=str, default=',', help='Provide separator for columns, default=,')

        neo4j = sub_parser.add_parser('neo4j', help='Read from Neo4j query write to XSV')
        neo4j.add_argument('user', type=str, help='Neo4j user to connect')
        neo4j.add_argument('query', type=str, help='Provide query to return tabular data')
        neo4j.add_argument('-H', '--host', type=str, default='127.0.0.1',
                           help='Neo4j host to connect, default=127.0.0.1')
        neo4j.add_argument('-p', '--port', type=int, default=7687, help='Neo4j port to connect, default=7687')
        neo4j.add_argument('-o', '--outfile', type=str, default=out_file,
                           help='Provide path to output XSV file, default=output_datetime.csv')
        neo4j.add_argument('-e', '--encoding', type=str, default='utf-8',
                           help='Provide encoding for output XSV file, default=utf-8')
        neo4j.add_argument('-s', '--separator', type=str, default=',', help='Provide separator for columns, default=,')

        self.args = parser.parse_args()

    @staticmethod
    def csv2xsv(**kwargs: dict) -> pd.DataFrame:
        """."""

        return pd.read_csv(kwargs['path'])

    @staticmethod
    def excel2xsv(**kwargs: dict) -> pd.DataFrame:
        """."""

        return pd.read_excel(kwargs['path'], sheet_name=kwargs['sheet'])

    @staticmethod
    def sqlite2xsv(**kwargs: dict) -> pd.DataFrame:
        """."""

        with sqlite3.connect(kwargs['path']) as connection:
            df: pd.DataFrame = pd.read_sql_query(kwargs['query'], con=connection)
        return df

    @staticmethod
    def mysql2xsv(**kwargs: dict) -> pd.DataFrame:
        """."""

        password: str = getpass(prompt='Password: ', stream=None)
        with Connection(host=kwargs['host'], port=kwargs['port'], user=kwargs['user'], passwd=password, db=kwargs['database']) as connection:
            df: pd.DataFrame = pd.read_sql(kwargs['query'], con=connection)
        return df

    @staticmethod
    def neo4j2xsv(**kwargs: dict) -> pd.DataFrame:
        """."""

        password: str = getpass(prompt='Password: ', stream=None)
        uri: str = 'bolt://{}:{}'.format(kwargs['host'], kwargs['port'])
        driver = GraphDatabase.driver(uri, auth=(kwargs['user'], password))
        with driver.session() as session:
            records = session.run(kwargs['query'])
        return pd.DataFrame([record.values() for record in records], columns=records.keys())

    def run(self) -> None:
        """."""

        call: dict = {
            'csv': self.csv2xsv,
            'excel': self.excel2xsv,
            'sqlite': self.sqlite2xsv,
            'mysql': self.mysql2xsv,
            'neo4j': self.neo4j2xsv,
        }

        if self.args.command not in call:
            sys.exit('Please enter a sub command, for help use -h flag')

        df: pd.DataFrame = call[self.args.command](**vars(self.args))
        df.to_csv(self.args.outfile, index=self.index, sep=self.args.separator, encoding=self.args.encoding)


if __name__ == '__main__':
    """."""

    try:
        table2xsv: Table2XSV = Table2XSV()
        table2xsv.run()

    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print('{}: {}'.format(tc.__name__, exc))
