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
        if kwargs["path"].endswith(".csv"):
            _df = pd.read_csv(kwargs["path"])
            _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)
        else:
            print("Invalid file, can only accept files ending with .csv")

    def excel2xsv(self, **kwargs):
        if kwargs["path"].endswith(".xlsx"):
            _df = pd.read_excel(kwargs["path"], sheet_name=kwargs["sheet"])
            _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)
        else:
            print("Invalid file, can only accept files ending with .xlsx")

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
        parser.add_argument("params", nargs="+", help="table type to convert to XSV and respective config")
        parser.add_argument("-o", "--outfile", default="output {}.csv".format(datetime.now()),
                            help="provide name for the output file with extension as .csv")
        parser.add_argument("-e", "--encoding", default="utf-8", help="provide an encoding enclosed in quotes")
        parser.add_argument("-s", "--sep", default=",", help="provide a separator enclosed in quotes")
        args = parser.parse_args()

        t2xsv = Table2XSV(args.outfile, args.sep, args.encoding)

        if len(args.params) == 1:
            print("Please refer command line args help by using -h or --help or go through the manual")

        else_print = "Incorrect Number or Order of Arguments"

        if args.params[0].lower() == "csv":
            if len(args.params) == 2:
                t2xsv.csv2xsv(path=args.params[1])
            else:
                print(else_print)
        elif args.params[0].lower() == "excel":
            if len(args.params) == 3:
                t2xsv.excel2xsv(path=args.params[1], sheet=args.params[2])
            else:
                print(else_print)
        elif args.params[0].lower() == "sqlite":
            if len(args.params) == 3:
                t2xsv.sqlite2xsv(path=args.params[1], query=args.params[2])
            else:
                print(else_print)
        elif args.params[0].lower() == "mysql":
            if len(args.params) == 7:
                t2xsv.mysql2xsv(host=args.params[1], port=args.params[2], user=args.params[3], password=args.params[4],
                                db=args.params[5], query=args.params[6])
            else:
                print(else_print)
        else:
            print("Undefined input source")

    except Exception as e:
        print(e)
        tc, te, tb = sys.exc_info()
        print("Class: {} | Error: {} | Line Number: {}".format(tc, te, tb.tb_lineno))
