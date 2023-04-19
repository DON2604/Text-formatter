#     I have created this file Mrinmay
from django.http import HttpResponse
def index(request):
    return HttpResponse('''Home-page <a href= "removepunc">remo</a>''')

def removepunc(request):
    return HttpResponse('''removepunc  <a href= "/">back</a>''')

def capfirst(request):
    return HttpResponse('''captalize it <a href= "/">back</a>''')

def spacerem(request):
    return HttpResponse('''space removal <a href= "/">back</a>''')

def counter(request):
    return HttpResponse('''word counter <a href= "/">back</a>''')

