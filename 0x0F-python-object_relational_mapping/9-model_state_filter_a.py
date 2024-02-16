#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id). \
            filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()
