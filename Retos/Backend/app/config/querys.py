from config.db import engine
from httpx import AsyncClient

async def get_all(table):
    """get_all function
    This function get all data from a table

    Args:
        table: table to get data from

    Returns:
        [List]: list of data from table
    """
    with engine.connect() as conn:
        return conn.execute(table.select()).fetchall()

async def get_one(table, name):
    with engine.connect() as conn:
        return  conn.execute(table.select().where(table.c.name == name)).fetchone()

async def get_one_user(table, id):
    with engine.connect() as conn:
        return  conn.execute(table.select().where(table.c.id == id)).fetchone()

async def get_dogs_adopted():
    with engine.connect() as conn:
        return  conn.execute('SELECT * FROM dogs WHERE is_adopted = 1').fetchall()

async def create_object(table, data):
    with engine.connect() as conn:
        conn.execute(table.insert().values(data))

async def update_dog(table, name, dict):
    with engine.connect() as conn:
        conn.execute(table.update().values(dict).where(table.c.name == name))

async def update_user(table, id, dict):
    with engine.connect() as conn:
        conn.execute(table.update().values(dict).where(table.c.id == id))

async def delete_dog(table, name):
    with engine.connect() as conn:
        conn.execute(table.delete().where(table.c.name == name))

async def delete_user(table, id):
    with engine.connect() as conn:
        conn.execute(table.delete().where(table.c.id == id))


async def dogs_by_user(user_id):
    with engine.connect() as conn:
        return  conn.execute('SELECT * FROM dogs WHERE user_id = {}'.format(user_id)).fetchall()
    


async def get_picture():
    async with AsyncClient() as client:
        response = await client.get("https://dog.ceo/api/breeds/image/random")
        return response.json()["message"]