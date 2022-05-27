from tortoise import Tortoise


async def app_init():
    """create database"""
    await Tortoise.init(
        db_url='sqlite://indeces.db',
        modules={'Indice': ['server.database.indices']}
    )
    await Tortoise.generate_schemas()
