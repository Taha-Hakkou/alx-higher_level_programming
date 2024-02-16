#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine, delete)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    delete = delete(State).where(State.name.like('%a%'))
    with engine.connect() as connect:
        result = connect.execute(delete)
        connect.commit()
    session.close()
