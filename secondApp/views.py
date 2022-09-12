from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def displayInput(request):
    return HttpResponse("<input type='text' placeholder='Ingrese usuario'>")

def displayLink(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=Lk3WAFqNzPw'><a/>")