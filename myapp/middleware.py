# 1- read this article: 
# https://docs.djangoproject.com/en/5.0/topics/http/middleware/
# 2- see the MiddlewareMixin implementation
# 3- create another middleware without middleware mixin (filtre IP addresses)
import time
from django.utils.deprecation import MiddlewareMixin

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        print(f"request obj : {request}")
        print(f"Request method: {request.method}, Request path: {request.path}")

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        print(f"response obj: {response}")
        print(f"Request to {request.path} took {duration:.2f} seconds")
        return response
