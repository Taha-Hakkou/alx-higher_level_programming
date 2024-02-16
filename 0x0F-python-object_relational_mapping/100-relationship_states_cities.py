#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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
    myState = State(name='California')
    myCity = City(name='San Francisco', state_id=myState.id)
    myState.cities = [myCity]
    session.add(myState)
    session.add(myCity)
    session.commit()
    session.close()
