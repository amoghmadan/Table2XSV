import unittest

from table2xsv.bin import execute_from_command_line
from table2xsv.core import CommandError
from table2xsv.core.helpers import call_command
from table2xsv.management.commands.csv import Command
from table2xsv.utils.getter import get_name


class TestBaseCommand(unittest.TestCase):
    """Test Base Command"""

    def test_empty_base_command(self):
        """Test Empty Base Command"""

        argv = [get_name()]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_unknown_command(self):
        """Test Unknown Command"""

        argv = [get_name(), "unknown"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_help(self):
        """Test Version"""

        argv = [get_name(), "--help"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_help_by_class(self):
        """Test Help By Class"""

        with self.assertRaises(SystemExit):
            call_command(Command(), "--help", verbosity=0)

    def test_version(self):
        """Test Version"""

        argv = [get_name(), "--version"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_version_by_class(self):
        """Test Help By Class"""

        with self.assertRaises(SystemExit):
            call_command(Command(), "--version", verbosity=0)

    def test_commands_flag(self):
        """Test Commands Flag"""

        argv = [get_name(), "help", "--commands"]
        self.assertEqual(execute_from_command_line(argv), None)

    def test_possible_match(self):
        """Test Command Error"""

        argv = [get_name(), "xsv"]
        with self.assertRaises(SystemExit):
            execute_from_command_line(argv)

    def test_unknown_command_error(self):
        """Test Unknown Command Error"""

        with self.assertRaises(CommandError):
            call_command("unknown", verbosity=0)
