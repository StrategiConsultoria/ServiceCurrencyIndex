from tortoise import Tortoise


async def app_init():
    """create database"""
    await Tortoise.init(
        db_url='sqlite://index.db',
        modules={'Index': ['server.database.index']}
    )
    await Tortoise.generate_schemas()
