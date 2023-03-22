from django.http import HttpResponse

class PreventBackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.session.get('userid') is None:
            response['cache_control'] = 'no-cache'
        return response
