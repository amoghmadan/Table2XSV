import sys
import sqlite3

import typer
import pandas as pd
from MySQLdb import Connect
from neo4j import GraphDatabase

app = typer.Typer()


@app.command()
def csv(
    path: str,
    seperator: str = ',',
    encoding: str = 'utf-8',
    outfile: str = 'output.csv'
) -> None:
    """Convert CSV files to XSV"""

    df: pd.DataFrame = pd.read_csv(path)
    df.to_csv(outfile, sep=seperator, encoding=encoding, index=False)


@app.command()
def excel(
    path: str,
    sheet: str = 'Sheet1',
    seperator: str = ',',
    encoding: str = 'utf-8',
    outfile: str = 'output.csv'
) -> None:
    """Convert Excel Sheet to XSV"""

    df: pd.DataFrame = pd.read_excel(path, sheet_name=sheet)
    df.to_csv(outfile, sep=seperator, encoding=encoding, index=False)


@app.command()
def sqlite(
    path: str,
    query: str,
    seperator: str = ',',
    encoding: str = 'utf-8',
    outfile: str = 'output.csv'
) -> None:
    """Convert SQLite Table Query to XSV"""
    
    with sqlite3.connect(path) as connection:
        df: pd.DataFrame = pd.read_sql_query(query, con=connection)
    df.to_csv(outfile, sep=seperator, encoding=encoding, index=False)


@app.command()
def mysql(
    user: str,
    database: str,
    query: str,
    host: str = '127.0.0.1',
    port: int = 3306,
    seperator: str = ',',
    encoding: str = 'utf-8',
    outfile: str = 'output.csv'
) -> None:
        """Convert MySQL Table Query to XSV"""

        password: str = getpass(prompt='Password: ', stream=None)
        with Connection(host=host, port=port, user=user, passwd=password, db=database) as connection:
            df: pd.DataFrame = pd.read_sql(query, con=connection)
        df.to_csv(outfile, sep=seperator, encoding=encoding, index=False)


@app.command()
def neo4j(
    user: str,
    query: str,
    host: str = '127.0.0.1',
    port: int = 3306,
    seperator: str = ',',
    encoding: str = 'utf-8',
    outfile: str = 'output.csv'
) -> None:
        """Convert Neo4j Table Query to XSV"""

        password: str = getpass(prompt='Password: ', stream=None)
        uri: str = 'bolt://{}:{}'.format(kwargs['host'], kwargs['port'])
        driver = GraphDatabase.driver(uri, auth=(kwargs['user'], password))
        with driver.session() as session:
            records = session.run(kwargs['query'])
        df: pd.DataFrame = pd.DataFrame([record.values() for record in records], columns=records.keys())
        df.to_csv(outfile, sep=seperator, encoding=encoding, index=False)


if __name__ == '__main__':
    """."""

    app()
