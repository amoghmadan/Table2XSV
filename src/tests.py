from __future__ import annotations

import unittest
from pathlib import Path
from subprocess import run, CompletedProcess  # nosec
from sys import executable

from pandas import DataFrame

from main import Table2XSV


class TestTable2XSV(unittest.TestCase):
    """Test Table2XSV"""

    BASE_DIR: Path = Path(__file__).parent.parent
    ASSETS_DIR: Path = BASE_DIR / "assets"

    def test_csv2df(self: TestTable2XSV) -> None:
        """Test CSV"""

        kwargs: dict = {
            "path": self.ASSETS_DIR / "input.csv",
        }
        result: DataFrame = Table2XSV.csv2df(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    def test_excel2df(self: TestTable2XSV) -> None:
        """Test Excel"""

        kwargs: dict = {
            "path": self.ASSETS_DIR / "input.xlsx",
            "sheet": "Sheet1",
        }
        result: DataFrame = Table2XSV.excel2df(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    def test_sqlite2df(self: TestTable2XSV) -> None:
        """Test SQLite"""

        kwargs: dict = {
            "path": self.ASSETS_DIR / "input.sqlite3",
            "query": "SELECT 1 AS One;",
        }
        result: DataFrame = Table2XSV.sqlite2df(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    @unittest.skip("MySQL, Switch Test Credentials")
    def test_mysql2df(self: TestTable2XSV) -> None:
        """Test MySQL"""

        kwargs: dict = {
            "user": "root",
            "password": "root",
            "query": "SELECT 1 AS One;",
        }
        result: DataFrame = Table2XSV.mysql2df(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    @unittest.skip("Neo4j, Switch Test Credentials")
    def test_neo4j2df(self: TestTable2XSV) -> None:
        """Test Neo4j"""

        kwargs: dict = {
            "user": "neo4j",
            "password": "neo4j",
            "query": "MATCH 1 AS One;",
        }
        result: DataFrame = Table2XSV.neo4j2df(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    def test_version(self: TestTable2XSV) -> None:
        """Test Version"""

        cp: CompletedProcess = run([executable, "main.py", "-v"])
        self.assertEqual(cp.returncode, 0)

    def test_help(self: TestTable2XSV) -> None:
        """Test Help"""

        cp: CompletedProcess = run([executable, "main.py", "-h"])
        self.assertEqual(cp.returncode, 0)

    def test_empty_command(self: TestTable2XSV) -> None:
        """Test Empty Command"""

        cp: CompletedProcess = run([executable, "main.py"])
        self.assertEqual(cp.returncode, 1)
