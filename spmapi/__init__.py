# -*- coding: utf-8 -*-
import inspect

# import sanic Libraries
import sanic
app = sanic.Sanic(__name__)

# import spmapi blueprints
import spmapi.handlers  # noqa: F402

# import spmapi helpers
import spmapi.utils.exceptions  # noqa: F402


def isblueprint(obj):
    return isinstance(obj, sanic.Blueprint)


for mname, module in inspect.getmembers(spmapi.handlers, inspect.ismodule):
    for hname, handler in inspect.getmembers(module, inspect.ismodule):
        for bpname, blueprint in inspect.getmembers(
            handler, predicate=isblueprint
        ):
            app.blueprint(blueprint)
