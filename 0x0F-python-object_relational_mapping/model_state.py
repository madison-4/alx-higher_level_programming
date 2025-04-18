#!/usr/bin/python3
""" A module that defines a state class and an instance of base
    It links to the MySQL table states
    uses port 3306
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


db_url = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"+
f"@localhost:3306/{sys.argv[3]}"
engine = create_engine(db_url, echo=True)
Base = declarative_base()


class State(Base):
    """ A class that maps to the states table
        This class will define the table
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
