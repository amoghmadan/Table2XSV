from __future__ import annotations

from datetime import datetime

from table2xsv.core.base import BaseCommand
from table2xsv.utils.getter import get_version


class Table2XSVBaseCommand(BaseCommand):
    """Optional Arguments Base Command"""

    index = False
    version = get_version()

    def add_command_arguments(self, parser):
        """Add Command Specific Arguments"""

        raise NotImplementedError(
            "subclasses of %s must provide a add_command_arguments() method"
            % (self.__class__.__name__,)
        )

    def add_arguments(self, parser):
        """Add Optional Arguments for all the Commands"""

        now = datetime.now().strftime("%Y-%m-%dT%H-%M-%S.%fZ")

        self.add_command_arguments(parser)
        parser.add_argument(
            "-o",
            "--outfile",
            type=str,
            default="output-[%s].csv" % (now,),
            help="Provide path to output XSV file, default=output-[datetime].csv",
        )
        parser.add_argument(
            "-e",
            "--encoding",
            type=str,
            default="utf-8",
            help="Provide encoding for output XSV file, default=utf-8",
        )
        parser.add_argument(
            "-s",
            "--separator",
            type=str,
            default=",",
            help="Provide separator for columns, default=,",
        )

    def process_to_df(self, *args, **options):
        """Process to DataFrame"""

        raise NotImplementedError(
            "subclasses of %s must provide a process2df() method"
            % (self.__class__.__name__,)
        )

    def process_outfile(self, df, **options):
        """Create XSV File from DataFrame"""

        df.to_csv(
            options["outfile"],
            index=self.index,
            sep=options["separator"],
            encoding=options["encoding"],
        )

    def handle(self, *args, **options):
        """The actual logic of the command. Subclasses must implement this method."""

        df = self.process_to_df(*args, **options)
        self.process_outfile(df, **options)
