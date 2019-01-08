from django.utils import timezone
from django.http import JsonResponse
from HeyM8.settings import LOGIN_URL


def ajax_login_required(view):

    def wrapper(request, *args, **kwargs):
        if request.is_ajax() and (not request.user.is_authenticated):
            return JsonResponse({"redirectTo":LOGIN_URL, "isNotAuthenticated":True})
        return view(request, *args, **kwargs)

    return wrapper
