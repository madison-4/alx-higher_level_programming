#!/usr/bin/python3
""" A module to add the louisiana state to the db
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def statesprint(username, password, database):
    """ This function adds the Louisian state
    the in prints them.
    """

    dburl = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(dburl, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    print(f'{new_state.id}')
    session.close


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Incorrect number of arguments")
        sys.exit(1)
    username, password, database = sys.argv[1:4]
    statesprint(username, password, database)
