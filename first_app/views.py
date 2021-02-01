from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"first_app/index.html")

def mallika(request):
    return HttpResponse("mallika, hello")

def shlagha(request):
    return HttpResponse("shlagha, hello") 

def greet(request, name):
     return render(request, "first_app/greet.html", {"name": name.capitalize(),"id":id})

def greet_hello(request, name):
    hello = "Hello, How Are You"
    id=2
    
    return  HttpResponseRedirect(reverse("greet", kwargs={"id":id}))