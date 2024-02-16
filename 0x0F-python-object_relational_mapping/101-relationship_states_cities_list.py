#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda x: x.id):
            print("\t{}: {}".format(city.id, city.name))
    session.close()
