#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
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
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
