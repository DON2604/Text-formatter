#     I have created this file Mrinmay
from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1>Konnichiwa<h1/> <br> <a href="https://github.com/DON2604"> superrr <a/>''')

def about(request):
    return HttpResponse("Hello Everynyan")