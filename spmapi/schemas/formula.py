# -*- coding: utf-8 -*-
import marshmallow


class MinimumVersion(marshmallow.fields.Str):

    def _serialize(self, val, attr, data):
        return '.'.join(map(str, val))


class OsList(marshmallow.fields.List):

    def _serialize(self, val, attr, data):
        return val.split(', ')


class ExtraInfo(marshmallow.Schema):

    os = OsList(marshmallow.fields.Str, required=True)
    os_family = OsList(marshmallow.fields.Str, required=True)
    summary = marshmallow.fields.Str(required=True)
    description = marshmallow.fields.Str(required=True)


class Formula(marshmallow.Schema):

    name = marshmallow.fields.Str(required=True)
    version = marshmallow.fields.Str(required=True)
    release = marshmallow.fields.Integer(required=True)
    minimum_version = MinimumVersion(required=True)
    extra_info = marshmallow.fields.Nested(ExtraInfo, required=True)
