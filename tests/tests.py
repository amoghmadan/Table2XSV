import os
import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.append(os.path.abspath(BASE_DIR))

try:
    from table2xsv.bin import execute_from_command_line
    from table2xsv.core import CommandError
    from table2xsv.core.helpers import call_command
    from table2xsv.management.commands.csv import Command
    from table2xsv.utils.getter import get_name
except ModuleNotFoundError:
    raise ModuleNotFoundError("Append BASE_DIR to sys.path list")

ASSETS_DIR = BASE_DIR / "assets"


class TestTable2XSV(unittest.TestCase):
    """Test Table2XSV"""

    name = get_name()

    def test_empty_base_command(self):
        """Test Empty Command"""

        argv = [self.name]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_empty_specific_command(self):
        """Test Empty Command"""

        argv = [self.name, "csv"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_unknown_command(self):
        """Test Unknown Command"""

        argv = [self.name, "unknown"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_version(self):
        """Test Version"""

        argv = [self.name, "--version"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_version_by_class(self):
        """Test Help By Class"""

        with self.assertRaises(SystemExit):
            call_command(Command(), "--version", verbosity=0)

    def test_version_by_command_name(self):
        """Test Help By Command Name"""

        with self.assertRaises(SystemExit):
            call_command("csv", "--version", verbosity=0)

    def test_help(self):
        """Test Version"""

        argv = [self.name, "--help"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_help_by_class(self):
        """Test Help By Class"""

        with self.assertRaises(SystemExit):
            call_command(Command(), "--help", verbosity=0)

    def test_possible_match(self):
        """Test Command Error"""

        argv = [self.name, "xsv"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_unknown_command_error(self):
        """Test Unknown Command Error"""

        with self.assertRaises(CommandError):
            call_command("unknown", verbosity=0)

    def test_unknown_args(self):
        """Test Unknown Command Error"""

        argv = [self.name, "csv", "path", "-l", "82"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_help_by_command_name(self):
        """Test Help By Command Name"""

        with self.assertRaises(SystemExit):
            call_command("csv", "--help", verbosity=0)

    def test_help_for_commands(self):
        """Test Commands Flag"""

        argv = [self.name, "help", "csv"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_commands_flag(self):
        """Test Commands Flag"""

        argv = [self.name, "help", "--commands"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_csv_command(self):
        """Test CSV"""

        options = {"path": os.path.abspath(ASSETS_DIR / "input.csv")}
        argv = [self.name, "csv", options["path"]]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_excel_command(self):
        """Test Excel"""

        options = {
            "path": os.path.abspath(ASSETS_DIR / "input.xlsx"),
            "sheet": "Sheet1",
        }
        argv = [self.name, "excel", options["path"], "-S", options["sheet"]]
        self.assertEqual(execute_from_command_line(argv), None)

    @unittest.skip("MySQL, Switch Test Credentials")
    def test_mysql_command(self):
        """Test MySQL"""

        options = {"user": "root", "password": "toor", "query": "SELECT 1 AS One;"}
        argv = [
            self.name,
            "mysql",
            options["user"],
            options["password"],
            options["query"],
        ]
        self.assertEqual(execute_from_command_line(argv), None)

    @unittest.skip("Neo4j, Switch Test Credentials")
    def test_neo4j_command(self):
        """Test Neo4j"""

        options = {
            "user": "neo4j",
            "password": "neo4j",
            "query": "MATCH 1 AS One;",
        }
        argv = [
            self.name,
            "neo4j",
            options["user"],
            options["password"],
            options["query"],
        ]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_sqlite_command(self):
        """Test SQLite"""

        options = {
            "path": os.path.abspath(ASSETS_DIR / "input.sqlite3"),
            "query": "SELECT id FROM One;",
        }
        argv = [self.name, "sqlite", options["path"], options["query"]]
        self.assertEqual(execute_from_command_line(argv), None)
