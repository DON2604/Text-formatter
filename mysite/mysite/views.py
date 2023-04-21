#     I have created this file Mrinmay
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def removepunc(request):
    txty=request.GET.get('text','default')
    print(txty)
    noice=request.GET.get('removepunc','off')
    print(noice)
    if noice == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in txty:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')


def capfirst(request):
    txty=request.GET.get('text','default')
    print(txty)
    noice=request.GET.get('capitalise','off')
    print(noice)
    if noice == "on":
        capitalized_string =""
        capitalized_string = txty.upper()
        params = {'purpose': 'capitalised', 'analyzed_text': capitalized_string}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

def spacerem(request):
    return HttpResponse('''space removal <a href= "/">home</a>''')


def counter(request):
    return HttpResponse('''word counter <a href= "/">home</a>''')

def carder(request):
    return HttpResponse('''name card <a href= "/">home</a>''')

def capi_view(request):
    return render(request, 'capi.html')