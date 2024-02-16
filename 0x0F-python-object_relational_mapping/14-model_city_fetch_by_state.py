#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import (create_engine, select)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    join = select(State.name, City.id, City.name).join(State)
    with engine.connect() as connect:
        result = connect.execute(join)
        for city in result:
            print("{}: ({}) {}".format(*city))
    session.close()
