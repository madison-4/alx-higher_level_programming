#!/usr/bin/python3
""" A module to print cities in ascending order by their city id
It prints cities from a db gicven to it
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def statesprint(username, password, database):
    """ This function connects to the database asks for the city record
    then in prints them.
    """

    dburl = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(dburl, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).\
        join(State, State.id == City.state_id).all()
    if cities:
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
    session.close


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Incorrect number pof arguments")
        sys.exit(1)
    username, password, database = sys.argv[1:4]
    statesprint(username, password, database)
