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
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `cities`.`name`, `states`.`name`\
              FROM `cities`\
              JOIN `states` ON `cities`.`state_id` = `states`.`id`\
              ORDER BY `cities`.`id` ASC;")
    places = c.fetchall()
    print(", ".join([city[0] for city in places if city[1] == sys.argv[4]]))
    c.close()
    db.close
