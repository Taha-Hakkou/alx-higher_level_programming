#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    usr, pw, db, state = sys.argv[1:5]
    myConnection = MySQLdb.connect(host="localhost", port=3306, user=usr,
                                   passwd=pw, db=db, charset="utf8")
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT cities.name FROM cities \
                      INNER JOIN states ON state_id = states.id \
                      WHERE states.name = %s \
                      ORDER BY cities.id ASC;", (state,))
    query_rows = myCursor.fetchall()
    print(', '.join([row[0] for row in query_rows]))
    myCursor.close()
    myConnection.close()
