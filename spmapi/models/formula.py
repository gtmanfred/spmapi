# -*- coding: utf-8 -*-
import sqlalchemy

import spmapi.models


Formula = sqlalchemy.Table(
    'formulas', spmapi.models.metadata,
    sqlalchemy.Column('id', sqlalchemy.types.BigInteger, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.types.Unicode),
    sqlalchemy.Column('major', sqlalchemy.types.SmallInteger),
    sqlalchemy.Column('minor', sqlalchemy.types.SmallInteger),
    sqlalchemy.Column('patch', sqlalchemy.types.SmallInteger),
    sqlalchemy.Column('release', sqlalchemy.types.SmallInteger),
    sqlalchemy.Column(
        'minimum_version',
        sqlalchemy.types.ARRAY(sqlalchemy.types.Integer)
    ),
    sqlalchemy.Column('extra_info', sqlalchemy.types.JSON),
    sqlalchemy.UniqueConstraint(
        'name', 'major', 'minor', 'patch', 'release',
        name='unique_releases'
    ),
)
