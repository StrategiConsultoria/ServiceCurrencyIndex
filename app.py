from server import create_app
import asyncio
from server.utils.controlers import update_database
import logging

logging.basicConfig(
    format='%(asctime)s - %(module)s - %(filename)s - %(message)s')

app = create_app()

if __name__ == '__main__':
    asyncio.run(update_database())
    app.run()
