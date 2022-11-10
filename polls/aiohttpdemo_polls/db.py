import aiopg.sa
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

category = Table(
    'category', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)))

subcategory = Table(
    'subcategory', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('category', ForeignKey('category.id')))

city = Table(
    'city', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)))

advert = Table(
    'advert', meta,
    Column('id', Integer, primary_key=True),
    Column('owner', Integer),
    Column('name', String(50)),
    Column('description', String(50)),
    Column('from_price', Integer),
    Column('email', String(50)),
    Column('wa_number', String(50)),
    Column('status', String(50)),
    Column('category', ForeignKey('category.id')),
    Column('subcategory', ForeignKey('subcategory.id')),
    Column('city', ForeignKey('city.id')))


# async def pg_context(app):
#     conf = app['config']['postgres']
#
#     engine = await aiopg.sa.create_engine(
#         database=conf['database'],
#         user=conf['user'],
#         password=conf['password'],
#         host=conf['host'],
#         port=conf['port'],
#         minsize=conf['minsize'],
#         maxsize=conf['maxsize'],
#     )
#     app['db'] = engine
#     yield
#
#
#     app['db'].close()
#     await app['db'].wait_closed()
