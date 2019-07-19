import os
from sanic import Sanic
from .controllers.logs import LogController


def create_app():
    app = Sanic()
    app.add_route(LogController.as_view(), '/api/logs')
    app.go_fast(debug=True, workers=os.cpu_count())
