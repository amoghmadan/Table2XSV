from sqlite3 import connect

from pandas import read_sql_query

from table2xsv.core import Table2XSVBaseCommand


class Command(Table2XSVBaseCommand):
    """SQLite Command"""

    help = "Read from SQLite Query write to XSV"

    def add_command_arguments(self, parser):
        """Add Arguments for SQLite Command"""

        parser.add_argument("path", type=str, help="Provide path of SQLite file")
        parser.add_argument(
            "query", type=str, help="Provide query to return tabular data"
        )

    def process_to_df(self, *args, **options):
        """SQLite Handling Logic"""

        with connect(options["path"]) as connection:
            df = read_sql_query(options["query"], con=connection)
        return df
