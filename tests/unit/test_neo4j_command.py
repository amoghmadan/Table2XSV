import unittest

from table2xsv.bin import execute_from_command_line
from table2xsv.core.helpers import call_command
from table2xsv.utils.getter import get_name


class TestNeo4jCommand(unittest.TestCase):
    """Test Neo4j Command"""

    command = "neo4j"

    def test_neo4j_command(self):
        """Test Neo4j"""

        options = {
            "user": "neo4j",
            "password": "neo4j",
            "query": "MATCH 1 AS One;",
        }
        argv = [
            get_name(),
            "neo4j",
            options["user"],
            options["query"],
            "-p",
            options["password"],
        ]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_help_by_command_name(self):
        """Test Help By Command Name"""

        with self.assertRaises(SystemExit):
            call_command(self.command, "--help", verbosity=0)

    def test_version_by_command_name(self):
        """Test Version By Command Name"""

        with self.assertRaises(SystemExit):
            call_command(self.command, "--version", verbosity=0)

    def test_unknown_args(self):
        """Test Unknown Command Error"""

        argv = [get_name(), self.command, "path", "-l", "82"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)
