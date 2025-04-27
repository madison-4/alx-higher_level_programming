#!/usr/bin/python3
"""A script that lists all objects from a databse given to it
It uses a mysql database and connects to it
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def printword():
    """ This function does the printing
    """
    use, word, dbase = sys.argv[1:]
    dburl = f"mysql+mysqldb://{use}:{word}@localhost:3306/{dbase}"
    engine = create_engine(dburl)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error, too few arguments")
        sys.exit(1)
    printword()
