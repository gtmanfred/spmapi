# -*- coding: utf-8 -*-
import sanic
import spmapi


class FileConflict(Exception):
    pass


@spmapi.app.exception(FileConflict)
async def file_already_exists(request, exception):
    return sanic.response.json(
        {'error': str(exception)},
        status=409,
    )


class NameMatchError(Exception):
    pass


@spmapi.app.exception(NameMatchError)
async def names_dont_match(request, exception):
    return sanic.response.json(
        {'error': str(exception)},
        status=400,
    )


class NoFormulaFile(Exception):
    pass


@spmapi.app.exception(NoFormulaFile)
async def no_formula_file(request, exception):
    return sanic.response.json(
        {'error': str(exception)},
        status=400,
    )
