from table2xsv.core import ManagementUtility


def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""

    utility = ManagementUtility(argv)
    utility.execute()
