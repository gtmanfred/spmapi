# -*- coding: utf-8 -*-
import sqlalchemy.ext.declarative

import spmapi.utils.database

Base = sqlalchemy.ext.declarative.declarative_base(
    bind=spmapi.utils.database.engine
)
Base.metadata.create_all(spmapi.utils.database.engine.sync_engine)
