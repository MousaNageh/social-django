from django.http import HttpResponseRedirect
import re


class FollowersMiddeware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if re.search("^/profile/\d+$", request.path):
            id = int(re.split("/", request.path)[2])
            if request.GET.get("followers"):
                if int(request.session["_auth_user_id"]) != id:
                    return HttpResponseRedirect("/")

        elif re.search("^/profile/userrequestsdetails/\d+$", request.path):
            id = int(re.split("/", request.path)[3])
            if int(request.session["_auth_user_id"]) != id:
                return HttpResponseRedirect("/")

        elif re.search("^/posts/\d+/edit/\d+$", request.path) or re.search("^/posts/\d+/delete/\d+$", request.path):
            id = int(re.split("/", request.path)[2])
            if int(request.session["_auth_user_id"]) != id:
                return HttpResponseRedirect("/")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
