#!/usr/bin/python3
"""A script that lists all objects from a databse given to it
It uses a mysql database and connects to it
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


use, word, dbase = sys.argv[1:4]
dburl = f"mysql+mysqldb://{use}:{word}@localhost:3306/{dbase}"
