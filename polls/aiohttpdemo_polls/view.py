from aiohttp import web

import db
from polls.aiohttpdemo_polls.main import app


async def index(request):
    return web.Response(text="Hello, world")




#save data to db
@app.post('/save_data')
async def save_data(request):
    data = await request.json()
    category = db.category(name='kalimaster', description='Gary',)
    print(data)
    return web.json_response({'status': 'ok'})