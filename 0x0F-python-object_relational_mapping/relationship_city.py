#!/usr/bin/python3
""" A module that defines a city class and an instance of base
    It links to the MySQL table cities
    uses port 3306
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


# ur = f"mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa"
# db_url = ur
# engine = create_engine(db_url, echo=True)


class City(Base):
    """ A class that maps to the states table
        This class will define the table
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    states_id = Column(ForeignKey("states.id"), nullable=False)

# Base.metadata.create_all(engine)
