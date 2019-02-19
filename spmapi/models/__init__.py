# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

import spmapi.utils.database

Base = sqlalchemy.ext.declarative.declarative_base()
Base.metadata.create_all(spmapi.utils.database.engine.sync_engine)
