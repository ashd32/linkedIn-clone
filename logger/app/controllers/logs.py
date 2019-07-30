from sanic.response import json
from sanic.views import HTTPMethodView
from datetime import date
from app.services.utils import process_logs

import os.path


class LogController(HTTPMethodView):
    
    async def post(self, request):
        filename = date.today()
        process_logs(filename, request)

        return json({"status":"200"})
        
        
        
