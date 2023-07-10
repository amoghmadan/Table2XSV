import os
import unittest

from table2xsv.bin import execute_from_command_line
from table2xsv.core.helpers import call_command
from table2xsv.utils.getter import get_name
from paths import ASSETS_DIR


class TestSQLiteCommand(unittest.TestCase):
    """Test SQLite Command"""

    command = "sqlite"

    def test_sqlite_command(self):
        """Test SQLite"""

        options = {
            "path": os.path.abspath(ASSETS_DIR / "input.sqlite3"),
            "query": "SELECT id FROM One;",
        }
        argv = [get_name(), self.command, options["path"], options["query"]]
        self.assertEqual(execute_from_command_line(argv), None)

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
