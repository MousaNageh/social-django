from django.http import HttpResponseRedirect
import re


class EditprofileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if re.search("^/profile/editprofile/\d+$", request.path):
            id = int(re.split("/", request.path)[3])
            if request.user.id != id:
                return HttpResponseRedirect("/")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
