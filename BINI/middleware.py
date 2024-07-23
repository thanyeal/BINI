# middleware.py
from django.utils.deprecation import MiddlewareMixin

class CacheControlMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'static' in request.path:
            response['Cache-Control'] = 'public, max-age=31536000'  # Cache for 1 year
        return response
