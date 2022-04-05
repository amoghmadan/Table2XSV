import sys
from getpass import getpass

try:
    import MySQLdb
except ModuleNotFoundError:
    msg = "Install optional dependency mysql, pip install table2xsv[mysql]"
    sys.exit(msg)
from pandas import read_sql

from table2xsv.core import CommandError, Table2XSVBaseCommand


class Command(Table2XSVBaseCommand):
    """MySQL Command"""

    help = "Read from MySQL Query write to XSV"

    def add_command_arguments(self, parser):
        """Add Arguments for MySQL Command"""

        parser.add_argument("user", type=str, help="MySQL user to connect")
        parser.add_argument("database", type=str, help="MySQL db to connect")
        parser.add_argument(
            "query", type=str, help="Provide query to return tabular data"
        )
        parser.add_argument(
            "-H",
            "--host",
            type=str,
            default="127.0.0.1",
            help="MySQL host to connect, default=127.0.0.1",
        )
        parser.add_argument(
            "-P",
            "--port",
            type=int,
            default=3306,
            help="MySQL port to connect, default=3306",
        )
        parser.add_argument(
            "-p", "--password", type=str, help="MySQL password to connect"
        )

    def process_to_df(self, *args, **options):
        """MySQL Handling Logic"""

        keys = ("host", "port", "user", "password", "database")
        if not options["password"]:
            options["password"] = getpass(prompt="Password: ", stream=None)
        credentials = {key: options[key] for key in keys}
        try:
            with MySQLdb.Connection(**credentials) as con:
                df = read_sql(options["query"], con=con)
            return df
        except Exception as e:
            raise CommandError(*e.args) from e
