from sanic.response import json
from sanic.views import HTTPMethodView


class LogController(HTTPMethodView):
    
    async def get(self, request):
        pass

    async def post(self, request):
        pass