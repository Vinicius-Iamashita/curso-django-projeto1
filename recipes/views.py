from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return HttpResponse('HOME 1')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
