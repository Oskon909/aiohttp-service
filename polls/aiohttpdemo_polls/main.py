from aiohttp import web

from settings import config
from routes import setup_routes

app = web.Application()
print(app)
setup_routes(app)
app['config'] = config
web.run_app(app )