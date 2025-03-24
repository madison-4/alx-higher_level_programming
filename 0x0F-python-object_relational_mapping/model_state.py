#!/usr/bin/python3
""" A script to list all states from a database
    The db, username and passwd are args
    It prints states whose names are the fourth argument
    prints ordered cities
"""

if __name__ == "__main__":
    """ The code should not be executed when imported
    """

    import sys
    import MySQLdb
    import SQLAlchemy
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    db.close
