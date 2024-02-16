#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    myConnection = MySQLdb.connect(host="localhost", port=3306, user=usr,
                                   passwd=pw, db=db, charset="utf8")
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM states \
                      WHERE name LIKE 'N%' ORDER BY id ASC;")
    query_rows = myCursor.fetchall()
    for row in query_rows:
        print(row)
    myCursor.close()
    myConnection.close()
