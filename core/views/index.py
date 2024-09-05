from core.views.base import *


def welcome(request: HttpRequest):
    return render(request, "front_end/welcome.html")
