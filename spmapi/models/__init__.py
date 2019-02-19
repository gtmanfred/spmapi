# -*- coding: utf-8 -*-
import sqlalchemy
import sqlalchemy.ext.declarative

import spmapi.utils.database

metadata = sqlalchemy.MetaData()
Base = sqlalchemy.ext.declarative.declarative_base(metadata=metadata)
Base.metadata.create_all(spmapi.utils.database.engine.sync_engine)
