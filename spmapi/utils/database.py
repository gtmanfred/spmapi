# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy_aio
import os


class Connect(object):
    def __new__(cls):
        if not hasattr(cls, 'engine'):
            cls.engine = sqlalchemy.create_engine(
                os.environ.get(
                    'SQL_ALCHEMY_URI',
                    'postgresql+psycopg2://postgres:postgres@localhost/spmapi'
                ),
                strategy=sqlalchemy_aio.ASYNCIO_STRATEGY,
            )
        return cls


engine = Connect().engine
Session = sqlalchemy.orm.sessionmaker(bind=engine.sync_engine)
