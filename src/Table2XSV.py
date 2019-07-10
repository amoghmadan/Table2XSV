""" Command Line tool to transform Table Data to XSV """
import argparse
from datetime import datetime
import sys
import MySQLdb
import neo4j
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
        return "Table2XSV(outfile, sep, encoding)"

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

    def mysql2xsv(self, **kwargs):
        _connection = MySQLdb.connect(host=kwargs["host"], port=int(kwargs["port"]), user=kwargs["user"],
                                      passwd=kwargs["password"], db=kwargs["db"])
        _df = pd.read_sql(kwargs["query"], con=_connection)
        _connection.close()
        _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)

    def neo4j2xsv(self, **kwargs):
        _driver = neo4j.GraphDatabase.driver("bolt://{}:{}".format(kwargs["host"], kwargs["port"]),
                                             auth=(kwargs["user"], kwargs["password"]))
        with _driver.session() as _session:
            _records = _session.run(kwargs["query"])
        _df = pd.DataFrame([_record.values() for _record in _records], columns=_records.keys())
        _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)

    def sqlite2xsv(self, **kwargs):
        if kwargs["path"].endswith(".db"):
            _connection = sqlite3.connect(kwargs["path"])
            _df = pd.read_sql_query(kwargs["query"], con=_connection)
            _connection.close()
            _df.to_csv(self.__outfile, index=self.__index, sep=self.__sep, encoding=self.__encoding)
        else:
            print("Invalid file, can only accept files ending with .db")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-o", "--outfile", default="output {}.csv".format(datetime.now()),
                            help="provide name for the output file (with extension as csv)")
        parser.add_argument("-s", "--sep", default=",", help="provide a separator")
        parser.add_argument("-e", "--encoding", default="utf-8", help="provide an encoding")

        parser.add_argument("--source_type",
                            help="provide source type, possible types csv, excel, mysql, neo4j and sqlite")
        parser.add_argument("--path", help="provide file path (csv, excel and sqlite only)")
        parser.add_argument("--sheet_name", help="provide sheet name (excel only)")
        parser.add_argument("--host", help="provide host (mysql and neo4j only)")
        parser.add_argument("--port", help="provide port (mysql and neo4j only)")
        parser.add_argument("--user", help="provide user (mysql and neo4j only)")
        parser.add_argument("--password", help="provide password (mysql and neo4j only)")
        parser.add_argument("--db", help="provide database name (mysql only)")
        parser.add_argument("--query", help="provide query (mysql, neo4j and sqlite only)")
        args = parser.parse_args()

        t2xsv = Table2XSV(args.outfile, args.sep, args.encoding)

        if args.source_type.lower() == "csv":
            t2xsv.csv2xsv(path=args.path)
        elif args.source_type.lower() == "excel":
            t2xsv.excel2xsv(path=args.path, sheet=args.sheet_name)
        elif args.source_type.lower() == "mysql":
            t2xsv.mysql2xsv(host=args.host, port=args.port, user=args.user, password=args.password, db=args.db,
                            query=args.query)
        elif args.source_type.lower() == "neo4j":
            t2xsv.neo4j2xsv(host=args.host, port=args.port, user=args.user, password=args.password, query=args.query)
        elif args.source_type.lower() == "sqlite":
            t2xsv.sqlite2xsv(path=args.path, query=args.query)
        else:
            print("Please refer command line args help module by using --help")

    except Exception as e:
        print(e)
        tc, te, tb = sys.exc_info()
        print("Class: {} | Error: {} | Line Number: {}".format(tc, te, tb.tb_lineno))
