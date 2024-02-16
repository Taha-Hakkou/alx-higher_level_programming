#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
