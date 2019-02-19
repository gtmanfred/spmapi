# -*- coding: utf-8 -*-
import spmapi.utils.tools as tools
import spmapi.schemas.formula
import sanic

bp = sanic.Blueprint(name='formulas', version=1)

formulas = spmapi.schemas.formula.Formula(many=True)


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
        {'message': 'success', 'formulas': formulas.dump(result).data},
        status=200
    )
