#!/usr/bin/python3

"""A module to get all staes from the given database
    The database and passwords are given as commandline arguments

    # a script to list all states from a database

    Attributes:
       The first arg is the user second, the password, third the database
"""

if __name__ == "__main__":
    """ This module should not be executed when imported
    """

    import sys
    import MySQLdb

    db = MySQLdb.connect(host=127.0.0.1: 3306, user=sys.argv[1],
    passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    states = cur.fetchall()
    for state in states:
        print(f"{state}")
