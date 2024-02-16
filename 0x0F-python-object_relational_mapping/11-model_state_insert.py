#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine, insert)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    usr, pw, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (usr, pw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    insert = insert(State).values(name='Louisiana')
    with engine.connect() as connect:
        result = connect.execute(insert)
        print(result.inserted_primary_key[0])
        connect.commit()
    session.close()
