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
    if (len(sys.argv) != 4):
        print("Can only take 3 arguments")
        sys.exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
              FROM `cities`\
              JOIN `states` ON `cities`.`state_id` = `states`.`id`\
              ORDER BY `cities`.`id` ASC;")
    places = c.fetchall()
    for city in places:
        print(city)
    c.close()
    db.close
