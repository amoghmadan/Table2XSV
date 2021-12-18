import sys

from pandas import read_excel

from table2xsv.management import Table2XSVBaseCommand


class Command(Table2XSVBaseCommand):
    """Excel Command"""

    help = "Read from Excel Sheet write to XSV"

    def add_command_arguments(self, parser):
        """Add Arguments for Excel Command"""

        parser.add_argument("path", type=str, help="Path to the Excel file")
        parser.add_argument(
            "-S",
            "--sheet",
            type=str,
            default="Sheet1",
            help="Provide name of sheet, default=Sheet1",
        )

    def process_to_df(self, *args, **options):
        """Excel Handling Logic"""

        try:
            return read_excel(options["path"], sheet_name=options["sheet"])
        except ImportError:
            msg = "Install optional dependency excel, pip install table2xsv[excel]"
            sys.exit(msg)
