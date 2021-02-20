from django.http import HttpResponseRedirect
import re


class RegisterLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path == '/login/' or request.path == '/register/':
            if request.session._session_key:
                return HttpResponseRedirect("/")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
