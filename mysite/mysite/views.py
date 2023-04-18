#     I have created this file Mrinmay
from django.http import HttpResponse
def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("removepunc")

def capfirst(request):
    return HttpResponse("captalise first")