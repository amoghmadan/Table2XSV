from __future__ import annotations

import sqlite3
import sys
from argparse import ArgumentParser, Namespace
from datetime import datetime
from getpass import getpass

from MySQLdb import Connection
from neo4j import GraphDatabase, Result
from pandas import read_csv, read_excel, read_sql, read_sql_query, DataFrame

__version__ = "1.0.0"


class Table2XSV(object, metaclass=type):
    """Table 2 XSV"""

    index: bool = False
    now: str = datetime.now().strftime("%Y-%m-%dT%H-%M-%S.%fZ")
    extra_optional_arguments: list = [
        {
            "short": "-o",
            "long": "--outfile",
            "type": str,
            "default": "output-[{now}].csv".format(now=now),
            "help": "Provide path to output XSV file, default=output-[datetime].csv",
        },
        {
            "short": "-e",
            "long": "--encoding",
            "type": str,
            "default": "utf-8",
            "help": "Provide encoding for output XSV file, default=utf-8",
        },
        {
            "short": "-s",
            "long": "--separator",
            "type": str,
            "default": ",",
            "help": "Provide separator for columns, default=,",
        },
    ]

    def __init__(self: Table2XSV) -> None:
        """Setup Parser and Sub-parsers"""

        # Parser / Sub Parser
        parser: ArgumentParser = ArgumentParser(description="Table 2 XSV")
        self.sub_parser = parser.add_subparsers(title="commands", dest="command")

        # Declare Sub Commands
        csv: ArgumentParser = self._csv_parser()
        excel: ArgumentParser = self._excel_parser()
        sqlite: ArgumentParser = self._sqlite_parser()
        mysql: ArgumentParser = self._mysql_parser()
        neo4j: ArgumentParser = self._neo4j_parser()

        # Add Extra Optional Arguments
        commands: list = [csv, excel, sqlite, mysql, neo4j]
        for command in commands:
            for entry in self.extra_optional_arguments:
                command.add_argument(
                    entry["short"],
                    entry["long"],
                    type=entry["type"],
                    default=entry["default"],
                    help=entry["help"],
                )

        # Get Arguments Passed By User
        self.args: Namespace = parser.parse_args()

    def _csv_parser(self) -> ArgumentParser:
        """CSV Arguments"""

        csv: ArgumentParser = self.sub_parser.add_parser(
            "csv", help="Read from XSV write to XSV"
        )
        csv.add_argument("path", type=str, help="Provide path of XSV file")
        return csv

    def _excel_parser(self) -> ArgumentParser:
        """Excel Arguments"""

        excel: ArgumentParser = self.sub_parser.add_parser(
            "excel", help="Read from Excel Sheet write to XSV"
        )
        excel.add_argument("path", type=str, help="Provide path of Excel file")
        excel.add_argument(
            "-S",
            "--sheet",
            type=str,
            default="Sheet1",
            help="Provide name of sheet, default=Sheet1",
        )
        return excel

    def _sqlite_parser(self) -> ArgumentParser:
        """SQLite Arguments"""

        sqlite: ArgumentParser = self.sub_parser.add_parser(
            "sqlite", help="Read from SQLite query write to XSV"
        )
        sqlite.add_argument("path", type=str, help="Provide path of SQLite file")
        sqlite.add_argument(
            "query", type=str, help="Provide query to return tabular data"
        )
        return sqlite

    def _mysql_parser(self) -> ArgumentParser:
        """MySQL Arguments"""

        mysql: ArgumentParser = self.sub_parser.add_parser(
            "mysql", help="Read from MySQL query write to XSV"
        )
        mysql.add_argument("user", type=str, help="MySQL user to connect")
        mysql.add_argument("database", type=str, help="MySQL db to connect")
        mysql.add_argument(
            "query", type=str, help="Provide query to return tabular data"
        )
        mysql.add_argument(
            "-H",
            "--host",
            type=str,
            default="127.0.0.1",
            help="MySQL host to connect, default=127.0.0.1",
        )
        mysql.add_argument(
            "-p",
            "--port",
            type=int,
            default=3306,
            help="MySQL port to connect, default=3306",
        )
        return mysql

    def _neo4j_parser(self) -> ArgumentParser:
        """Neo4j Arguments"""

        neo4j: ArgumentParser = self.sub_parser.add_parser(
            "neo4j", help="Read from Neo4j query write to XSV"
        )
        neo4j.add_argument("user", type=str, help="Neo4j user to connect")
        neo4j.add_argument(
            "query", type=str, help="Provide query to return tabular data"
        )
        neo4j.add_argument(
            "-H",
            "--host",
            type=str,
            default="127.0.0.1",
            help="Neo4j host to connect, default=127.0.0.1",
        )
        neo4j.add_argument(
            "-p",
            "--port",
            type=int,
            default=7687,
            help="Neo4j port to connect, default=7687",
        )
        return neo4j

    @staticmethod
    def csv2df(**kwargs: str) -> DataFrame:
        """Process CSV"""

        return read_csv(kwargs["path"])

    @staticmethod
    def excel2df(**kwargs: str) -> DataFrame:
        """Process Excel"""

        return read_excel(kwargs["path"], sheet_name=kwargs["sheet"])

    @staticmethod
    def sqlite2df(**kwargs: str) -> DataFrame:
        """Process SQLite"""

        with sqlite3.connect(kwargs["path"]) as connection:
            df: DataFrame = read_sql_query(kwargs["query"], con=connection)
        return df

    @staticmethod
    def mysql2df(**kwargs: str | int) -> DataFrame:
        """Process MySQL"""

        kwargs["passwd"] = getpass(prompt="Password: ", stream=None)
        with Connection(**kwargs) as connection:
            df: DataFrame = read_sql(kwargs["query"], con=connection)
        return df

    @staticmethod
    def neo4j2df(**kwargs: str | int) -> DataFrame:
        """Process Neo4j"""

        password: str = getpass(prompt="Password: ", stream=None)
        uri: str = "bolt://{host}:{port}".format(**kwargs)
        auth: tuple = (kwargs["uri"], password)
        with GraphDatabase.bolt_driver(uri, auth=auth) as driver:
            with driver.session() as session:
                records: Result = session.run(kwargs["query"])
        return DataFrame(
            [record.values() for record in records], columns=records.keys()
        )

    def run(self: Table2XSV) -> None:
        """Run"""

        call: dict = {
            "csv": self.csv2df,
            "excel": self.excel2df,
            "sqlite": self.sqlite2df,
            "mysql": self.mysql2df,
            "neo4j": self.neo4j2df,
        }

        if self.args.command not in call:
            sys.exit("Please enter a sub command, for help use -h flag")

        df: DataFrame = call[self.args.command](**vars(self.args))
        df.to_csv(
            self.args.outfile,
            index=self.index,
            sep=self.args.separator,
            encoding=self.args.encoding,
        )


def execute():
    """Execute"""

    try:
        table2xsv: Table2XSV = Table2XSV()
        table2xsv.run()
    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print("{klass}: {exception}".format(klass=tc.__name__, exception=exc))


if __name__ == "__main__":
    """Main"""

    execute()
