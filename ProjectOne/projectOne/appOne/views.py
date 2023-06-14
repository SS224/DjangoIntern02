from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def d1(request):

    return HttpResponse("<h1>Hello Django</h1>")

def d2(request):

    msg = "Hello Django FM"
    return HttpResponse(msg)

def d3(request):

    t = time.ctime()
    return HttpResponse(t)
