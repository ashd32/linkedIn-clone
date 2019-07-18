from django.utils.deprecation import MiddlewareMixin
import socket
import logging
import json
import time


logging.basicConfig(filename="sample.log", level=logging.INFO)
request_logger = logging.getLogger(__name__)


class RequestLogMiddleware(MiddlewareMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_request(self, request):
        if request.method in ['POST', 'PUT', 'PATCH']:
            request.req_body = request.req_body
        if str(request.get_full_path()).startswith('/api/'):
            request.start_time = time.time()

    def extract_log_info(self, request, exception, response=None):
        log_data = {
            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'run_time': time.time() - request.start_time,    
        }
        if request.method in ['PUT', 'POST', 'PATCH']:
            log_data['request_body'] = json.loads(
                str(request.req_body, 'utf-8')
            )
            if not response:
                if response['content-type'] == 'aplication/json':
                    response_body = response.content
                    log_data['response_body'] = response_body
        return log_data

    def process_response(self, request, response):
        if request.method != 'GET':
            if str(request.get_full_path()).startswith('/api/'):
                log_data = self.extract_log_info(request=request,
                                                 response=response)
                request_logger.debug(msg='work', extra=log_data)
                request_logger.warning("aaaaaaa")
        return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception:
            request_logger.exception(msg="Unhandled Exception")
        return exception
