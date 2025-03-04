#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
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
