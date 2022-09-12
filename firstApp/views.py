from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("<h1>BUENAS</h2>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora actual : </b>"+str(dt)
    return HttpResponse(s)