from sanic.response import json
from sanic.views import HTTPMethodView
from datetime import datetime
from app.services.utils import save_logs

import os.path


class LogController(HTTPMethodView):
    
    async def post(self, request):
        filename = datetime.today()
        print(request.body)
        if os.path.isfile('app/logs/{filename}.log'.format(filename=filename)):
            save_logs(filename, request.body)
        else:
            with open('app/logs/{filename}.log'.format(filename=filename), 'w') as f:
                f.write(request.body)
        
        
