from getpass import getpass

try:
    from neo4j import GraphDatabase
except ModuleNotFoundError:
    msg = "Install optional dependency neo4j, pip install table2xsv[neo4j]"
    raise ModuleNotFoundError(msg)
from pandas import DataFrame

from table2xsv.core import CommandError, Table2XSVBaseCommand


class Command(Table2XSVBaseCommand):
    """Neo4j Command"""

    help = "Read from Neo4j (Bolt) Tabular Query write to XSV"

    def add_command_arguments(self, parser):
        """Add Arguments for Neo4j Command"""
        parser.add_argument("user", type=str, help="Neo4j user to connect")
        parser.add_argument(
            "query", type=str, help="Provide query to return tabular data"
        )
        parser.add_argument(
            "-H",
            "--host",
            type=str,
            default="127.0.0.1",
            help="Neo4j host to connect, default=127.0.0.1",
        )
        parser.add_argument(
            "-P",
            "--port",
            type=int,
            default=7687,
            help="Neo4j bolt port to connect, default=7687",
        )
        parser.add_argument(
            "-p", "--password", type=str, help="Neo4j password to connect"
        )

    def process_to_df(self, *args, **options):
        """Neo4j Handling Logic"""
        if not options["password"]:
            options["password"] = getpass(prompt="Password: ", stream=None)
        uri = "bolt://%s:%d" % (options["host"], options["port"])
        auth = (options["user"], options["password"])
        with GraphDatabase.bolt_driver(uri, auth=auth) as driver:
            with driver.session() as session:
                try:
                    records = session.run(options["query"])
                except Exception as e:
                    raise CommandError(*e.args) from e
        return DataFrame([r.values() for r in records], columns=records.keys())
