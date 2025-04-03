#!/usr/bin/python3
""" A script to connect a class StaTE to the table sttes
    it connects to a MySQL server locally hosted
"""

if __name__ == "__main__":
    """ The code should not be executed when imported
    """

    import sys
    import MySQLdb
    from sqlalchemy import Column, Integer, String, create_engine
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                              sys.argv[2],
                                                              sys.argv[3])
    class State(Base):
        """ The state class for the states table
        """

        __tablename__ = "states"
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        
