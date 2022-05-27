from server import create_app
import logging

logging.basicConfig( format='%(asctime)s - %(module)s - %(filename)s - %(message)s')

app = create_app()
app.run()