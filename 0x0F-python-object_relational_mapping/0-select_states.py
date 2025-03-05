#!/usr/bin/python3
""" A script to list all states from a database
    The db, username and passwd are args
"""

if __name__ == "__main__":
    """ The code should not be executed when imported
    """

    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost:3306", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    states = c.fetchall()
    for state in states:
        print(state)
