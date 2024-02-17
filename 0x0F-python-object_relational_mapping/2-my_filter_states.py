#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':
    usr, pw, db, name = sys.argv[1:5]
    myConnection = MySQLdb.connect(host="localhost", port=3306, user=usr,
                                   passwd=pw, db=db, charset="utf8")
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM states \
                      WHERE name LIKE BINARY '{0}' \
                      ORDER BY id ASC;".format(name))
    query_rows = myCursor.fetchall()
    for row in query_rows:
        print(row)
    myCursor.close()
    myConnection.close()
