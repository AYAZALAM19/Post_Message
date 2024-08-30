from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("Welcome to my website!")

def homes(request):
    return render (request ,"index.html")

def layout(request):
    return render (request,'layout.html')