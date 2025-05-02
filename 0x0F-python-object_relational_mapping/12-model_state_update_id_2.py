#!/usr/bin/python3
""" A module to changes the name of a State
 It onkly changes without printing
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def statesprint(username, password, database):
    """ This function connects to the database asks for the state record
    then it vchanges its name. only the state with id of 2
    """

    dburl = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(dburl, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).one()
    states.name = "New Mexico"
    session.commit()
    session.close


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Incorrect number pof arguments")
        sys.exit(1)
    username, password, database = sys.argv[1:4]
    statesprint(username, password, database)
