from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.

def hello(r):
    return  HttpResponse("Hello <h1>world!<h1>")

def name(r):
    name = "Ainagul"
    return HttpResponse(f"Hello {name}")

def time(r):
    dt = datetime.now()
    return HttpResponse(f"NOW:{dt.strftime('%d-%m-%Y %H:%M:%S')}")

def age(r):
    age = "18"
    name = "Ainagul"
    return HttpResponse (f"Hello {name} ,your age:{age}")





