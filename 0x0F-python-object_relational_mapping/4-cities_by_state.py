#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    myConnection = MySQLdb.connect(host="localhost", port=3306, user=usr,
                                   passwd=pw, db=db, charset="utf8")
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                      INNER JOIN states ON state_id = states.id \
                      ORDER BY cities.id ASC;")
    query_rows = myCursor.fetchall()
    for row in query_rows:
        print(row)
    myCursor.close()
    myConnection.close()
