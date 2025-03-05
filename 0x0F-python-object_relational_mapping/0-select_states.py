#!/usr/bin/python3
import sys
import MySQLdb
""" A script to list all states from a database
    The db, username and passwd are args
"""

if __name__ == "__main__":
    """ The code should not be executed when imported
    """

    db = MySQLdb.connect(host=127.0.0.1: 3036, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    states = c.fetchall()
    for state in states:
        print(state)
