#!/usr/bin/python3
""" Task 12"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1],
                argv[2],
                argv[3]
                ),
            pool_pre_ping=True,
            echo=False
            )
    session = Session(engine)

    new_state = State()
    new_state.name = "Louisiana"
    session.query(State).filter(State.id == 2).update(
            {"name": "New Mexico"}, synchronize_session="fetch")
    session.commit()
