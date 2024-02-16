#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But safe from MySQL injections
"""
import MySQLdb
import sys


if __name__ == '__main__':
    usr, pw, db, name = sys.argv[1:5]
    myConnection = MySQLdb.connect(host="localhost", port=3306, user=usr,
                                   passwd=pw, db=db, charset="utf8")
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM states \
                      WHERE name = %s ORDER BY id ASC;", (name,))
    query_rows = myCursor.fetchall()
    for row in query_rows:
        print(row)
    myCursor.close()
    myConnection.close()
