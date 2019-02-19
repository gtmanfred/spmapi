# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()


def create_all(engine):
    Base.metadata.create_all(engine)
