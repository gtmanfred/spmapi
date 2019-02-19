# -*- coding: utf-8 -*-
import marshmallow


class Version(marshmallow.fields.Str):
    def _serialize(self, val, attr, data):
        print('version', val, attr, data)


class Formula(marshmallow.Schema):
    name = marshmallow.fields.Str(required=True)
    version = Version(required=True)
    release = marshmallow.fields.Integer(required=True)
