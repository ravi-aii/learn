from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brain(request):
    return HttpResponse("Hello brain!")

def david(request):
    return HttpResponse("Hello david!")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()} )

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")