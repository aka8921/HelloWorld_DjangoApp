from django.shortcuts import render
from django.http import HttpResponse

def ret(request):
    return HttpResponse('<h1>HELLO WORLD</h1>')

