from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Vik.  You're at the polls index.")
