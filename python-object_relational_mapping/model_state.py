#!/usr/bin/python3
""" Task 6 """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    ''' State class '''
    __tablename__ = 'states'
    id = Column(
            Integer, primary_key=True, unique=True,
            autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
