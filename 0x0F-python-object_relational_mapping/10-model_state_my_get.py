#!/usr/bin/python3
""" A module to print the state object with the name passed as an argument
    The name is the fourth argument
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def statesprint(username, password, database, state_name):
    """ This function connects to the database asks for the state record
    the in prints them.
    """

    dburl = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(dburl, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).all()
    if not states:
        print("Not found")
    else:
        for state in states:
            print(f"{state.id}")
    session.close


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Incorrect number of arguments")
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:5]
    statesprint(username, password, database, state_name)
