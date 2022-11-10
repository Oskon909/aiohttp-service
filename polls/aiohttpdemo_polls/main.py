from aiohttp import web

# from db import pg_context
from settings import config
from routes import setup_routes

app = web.Application()
print(app)
setup_routes(app)
app['config'] = config
# app.cleanup_ctx.append(pg_context)
print('iiiiiiiiiiiiiii')
web.run_app(app)