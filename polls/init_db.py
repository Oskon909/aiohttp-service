from sqlalchemy import create_engine,MetaData
from aiohttpdemo_polls.settings import config
from aiohttpdemo_polls.db import category, subcategory, city, advert

DSN = 'postgresql://postgres:akul6999@localhost:5432/aiohttpdemo_polls'

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[category, subcategory, city, advert])

def sample_data(engine):
    conn = engine.connect()
    conn.execute(category.insert(), [
        {'name': 'Категория 1'},
        {'name': 'Категория 2'},
        {'name': 'Категория 3'},
    ])
    conn.close()

if __name__ == "__main__":
    engine = create_engine(DSN)
    create_tables(engine)
    sample_data(engine)