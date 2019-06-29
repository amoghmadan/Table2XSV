""" Command Line tool to transform Table Data to XSV """
import argparse
from datetime import datetime
import sys
import MySQLdb
import pandas as pd
import sqlite3


class Table2XSV(object):
    """ Class to convert Table Data to XSV. """

    def __init__(self, outfile, sep, encoding):
        self.__outfile = outfile
        self.__sep = sep
        self.__index = False
        self.__encoding = encoding

    def __str__(self):
        return "Class to convert data from Excel, CSV, MySQL, SQLite to XSV."

    def __repr__(self):
        return "Table2XSV()"

    def csv2xsv(self, **kwargs):
        if kwargs["path"].endswith(".csv") or kwargs["path"].endswith(".tsv") or kwargs["path"].endswith(".psv"):
            _df = pd.read_csv(kwargs["path"])
            _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)
        else:
            print("Invalid file, can only accept files ending with .csv or .tsv or .psv")

    def excel2xsv(self, **kwargs):
        if kwargs["path"].endswith(".xlsx") or kwargs["path"].endswith(".xls"):
            _df = pd.read_excel(kwargs["path"], sheet_name=kwargs["sheet"])
            _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)
        else:
            print("Invalid file, can only accept files ending with .xlsx or .xls")

    def sqlite2xsv(self, **kwargs):
        if kwargs["path"].endswith(".db"):
            _connection = sqlite3.connect(kwargs["path"])
            _df = pd.read_sql_query(kwargs["query"], con=_connection)
            _connection.close()
            _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)
        else:
            print("Invalid file, can only accept files ending with .db")

    def mysql2xsv(self, **kwargs):
        _connection = MySQLdb.connect(host=kwargs["host"], port=int(kwargs["port"]), user=kwargs["user"],
                                      passwd=kwargs["password"], db=kwargs["db"])
        _df = pd.read_sql(kwargs["query"], con=_connection)
        _connection.close()
        _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("params", nargs="+", help="table type data to XSV with respective config")
        parser.add_argument("-o", "--outfile", default="output {}.csv".format(datetime.now()),
                            help="provide name for the output file with extension")
        parser.add_argument("-s", "--sep", default=",", help="provide a separator enclosed in quotes")
        parser.add_argument("-e", "--encoding", default="utf-8", help="provide an encoding enclosed in quotes")
        args = parser.parse_args()

        t2xsv = Table2XSV(args.outfile, args.sep, args.encoding)

        if len(args.params) == 1:
            print("Please refer command line args help by using --help or go through the manual")

        if args.params[0].lower() == "csv" and len(args.params) == 2:
            t2xsv.csv2xsv(path=args.params[1])
        elif args.params[0].lower() == "excel" and len(args.params) == 3:
            t2xsv.excel2xsv(path=args.params[1], sheet=args.params[2])
        elif args.params[0].lower() == "sqlite" and len(args.params) == 3:
            t2xsv.sqlite2xsv(path=args.params[1], query=args.params[2])
        elif args.params[0].lower() == "mysql" and len(args.params) == 7:
            t2xsv.mysql2xsv(host=args.params[1], port=args.params[2], user=args.params[3], password=args.params[4],
                            db=args.params[5], query=args.params[6])
        else:
            print("Either undefined input source, or incorrect number / order of arguments")

    except Exception as e:
        print(e)
        tc, te, tb = sys.exc_info()
        print("Class: {} | Error: {} | Line Number: {}".format(tc, te, tb.tb_lineno))
