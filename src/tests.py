from __future__ import annotations

import unittest
from pathlib import Path

from pandas import DataFrame

from main import Table2XSV


class TestTable2XSV(unittest.TestCase):
    """Test Table 2 XSV"""

    BASE_DIR: Path = Path(__file__).parent.parent
    ASSETS_DIR: Path = BASE_DIR / "assets"
    OUTFILE: str = "output.csv"

    def setUp(self: TestTable2XSV) -> None:
        """Set Up Instance"""

        self.file: Path = Path(self.OUTFILE).resolve()

    def tearDown(self: TestTable2XSV) -> None:
        """Tear Down Instance"""

        self.file.unlink(missing_ok=True)

    def test_csv(self: TestTable2XSV) -> None:
        """Test CSV"""

        kwargs: dict = {
            "path": self.ASSETS_DIR / "input.csv",
            "outfile": self.OUTFILE,
        }
        result: DataFrame = Table2XSV.csv2xsv(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    def test_excel(self: TestTable2XSV) -> None:
        """Test Excel"""

        kwargs: dict = {
            "path": self.ASSETS_DIR / "input.xlsx",
            "sheet": "Sheet1",
            "outfile": self.OUTFILE,
        }
        result: DataFrame = Table2XSV.excel2xsv(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    def test_sqlite(self: TestTable2XSV) -> None:
        """Test SQLite"""

        kwargs: dict = {
            "path": self.ASSETS_DIR / "input.sqlite3",
            "query": "SELECT 1 AS One;",
            "outfile": self.OUTFILE,
        }
        result: DataFrame = Table2XSV.sqlite2xsv(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    @unittest.skip("MySQL Different Machine")
    def test_mysql(self: TestTable2XSV) -> None:
        """Test MySQL"""

        kwargs: dict = {
            "user": "root",
            "password": "root",
            "query": "SELECT 1 AS One;",
            "outfile": self.OUTFILE,
        }
        result: DataFrame = Table2XSV.mysql2xsv(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))

    @unittest.skip("Neo4j Different Machine")
    def test_neo4j(self: TestTable2XSV) -> None:
        """Test Neo4j"""

        kwargs: dict = {
            "user": "neo4j",
            "password": "neo4j",
            "query": "MATCH 1 AS One;",
            "outfile": self.OUTFILE,
        }
        result: DataFrame = Table2XSV.neo4j2xsv(**kwargs)
        self.assertTrue(isinstance(result, DataFrame))
