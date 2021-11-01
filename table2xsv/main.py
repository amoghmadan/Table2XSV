import sys

from table2xsv.core.management.utility import ManagementUtility


def main():
    """Main"""

    utility = ManagementUtility(sys.argv)
    utility.execute()
