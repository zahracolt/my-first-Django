from django.shortcuts import render
django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello guys, Welcome to my Fashion App Hurray!")
