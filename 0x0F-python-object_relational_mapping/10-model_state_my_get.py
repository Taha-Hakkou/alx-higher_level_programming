#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db, name = sys.argv[1:5]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).where(State.name == "{}".format
                                       ((name,)[0])).one_or_none()
    if (state is not None):
        print("{}".format(state.id))
    else:
        print('Not found')
    session.close()
