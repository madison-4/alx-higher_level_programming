#!/usr/bin/python3
""" A module to print states in ascending order by the state
 whose name is given as the fourth argument
It is also free from sql injections
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

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")
    session.close


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Incorrect number pof arguments")
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:5]
    statesprint(username, password, database, state_name)
