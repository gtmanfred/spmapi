# -*- coding: utf-8 -*-
import sqlalchemy

import spmapi.models


class Formula(spmapi.models.Base):

    __tablename__ = 'formulas'

    id = sqlalchemy.Column(sqlalchemy.types.BigInteger, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.types.Unicode)
    major = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
    minor = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
    patch = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
    release = sqlalchemy.Column(sqlalchemy.types.SmallInteger)
    minimum_version = sqlalchemy.Column(
        sqlalchemy.types.ARRAY(sqlalchemy.types.Integer)
    )
    extra_info = sqlalchemy.Column(sqlalchemy.types.JSON)

    __table_args__ = (
        sqlalchemy.UniqueConstraint(
            'name', 'major', 'minor', 'patch', 'release',
            name='unique_releases'
        ),
    )

    @property
    def filename(self):
        return '-'.join([
            self.name,
            '.'.join([self.major, self.minor, self.patch]),
            self.release
        ]) + '.spm'
