#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine, update)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    update = update(State).where(State.id == 2).values(name='New Mexico')
    with engine.connect() as connect:
        result = connect.execute(update)
        connect.commit()
    session.close()
