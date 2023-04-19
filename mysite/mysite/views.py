#     I have created this file Mrinmay
from django.http import HttpResponse
def index(request):
    return HttpResponse("Home-page")

def removepunc(request):
    return HttpResponse("removepunc  <a href="">")

def capfirst(request):
    return HttpResponse("captalize it")

def spacerem(request):
    return HttpResponse("space removal")

def counter(request):
    return HttpResponse("word counter")

