#!/usr/bin/python3
""" A module to print the first state in the states
It prints states from a db gicven to it
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def statesprint(username, password, database):
    """ This function connects to the database asks for the state record
    the in prints them.
    """

    dburl = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(dburl, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).first()

    if not states:
        print("Nothing")

    else:
        print(f"{states.id}: {states.name}")
    session.close


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Incorrect number pof arguments")
        sys.exit(1)
    username, password, database = sys.argv[1:4]
    statesprint(username, password, database)
