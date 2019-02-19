# -*- coding: utf-8 -*-
import spmapi.utils.tools as tools
import sanic

bp = sanic.Blueprint(name='formulas', version=1)


@bp.post('/formulas')
async def upload_formula(request):
    if not request.files:
        return sanic.response.json(
            {'error': 'No files uploaded'},
            status=400
        )

    for name, archive in request.files.items():
        await tools.upload(
            name=name,
            spmfile=archive[0]
        )

    return sanic.response.json(
        {'message': 'success'},
        status=200
    )


@bp.get('/formulas')
async def list_formula(request):
    name = request.form.get('name')

    result = await tools.list_formulas(name)
    return sanic.response.json(
        {'message': 'success', 'formulas': result},
        status=200
    )
