from view import index, index2


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/index2', index2)