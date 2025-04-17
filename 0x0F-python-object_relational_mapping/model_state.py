#!/usr/bin/python3
""" A module that defines a state class and an instance of base
    It links to the MySQL table states
    uses port 3306
"""

from sqlalchemy import create_engine
import sys

db_url = f"mysql+mysqldb://{sys.argv[1]}:{sys.qrv[2]}@localhost:3306/{sys.argv[3]}"
engine = create_engine(db_url,echo=True)

