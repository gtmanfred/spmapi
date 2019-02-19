# -*- coding: utf-8 -*-
import aiobotocore
import asyncio
import io
import os
import sqlalchemy
import tarfile
import yaml

from spmapi.models.formula import Formula
from spmapi.utils.exceptions import (
    NameMatchError, FileConflict, NoFormulaFile
)

from spmapi.utils.database import engine, Session


async def upload(name, spmfile):
    '''
    upload spm file to digital ocean spaces
    '''
    bucket = 'spm-formulas'
    path = os.path.join(name, spmfile.name)

    try:
        formula = yaml.safe_load(tarfile.open(
            fileobj=io.BytesIO(spmfile.body)
        ).extractfile(
            os.path.join(name, 'FORMULA')
        ))
    except KeyError:
        raise NoFormulaFile(
            f'Unable to find formula file in SPM: {name}/FORMULA'
        )

    fname = formula.pop('name')
    if fname != name:
        raise NameMatchError(f'Names do not match: {name} != {fname}')

    version, release = formula.pop('version'), formula.pop('release')
    major, minor, patch = map(int, version.split('.'))

    try:
        async with engine.connect() as session:
            await session.execute(sqlalchemy.insert(Formula).values(
                name=name,
                major=major, minor=minor, patch=patch,
                release=release,
                minimum_version=[
                    num for num in map(
                        int, str(formula.pop('minimum_version')).split('.')
                    )
                ],
                extra_info=formula,
            ))
    except sqlalchemy.exc.IntegrityError:
        raise FileConflict(
            f'Formula already exists: {name}=={version}-{release}'
        )

    loop = asyncio.get_event_loop()
    session = aiobotocore.get_session(loop=loop)
    async with session.create_client(
        's3', region_name='sfo2',
        endpoint_url='https://sfo2.digitaloceanspaces.com',
        aws_secret_access_key=os.environ.get('DO_SECRET_ACCESS_KEY'),
        aws_access_key_id=os.environ.get('DO_ACCESS_KEY_ID'),
    ) as client:
        await client.put_object(Bucket=bucket, Key=path, Body=spmfile.body)


async def list_formulas(name=None):
    session = Session()
    query = session.query(Formula)
    if name is not None:
        query = query.filter_by(Formula.name == name)
    return (
        query
        .order_by(Formula.name)
        .order_by(Formula.major.desc())
        .order_by(Formula.minor.desc())
        .order_by(Formula.patch.desc())
        .order_by(Formula.release.desc())
        .all()
    )
