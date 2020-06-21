from django.shortcuts import render
from django.http import request, HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Backend good!"
                        "<h1><p>Congrats on deployment to azure</p></h1>")

def another(request):
    return render(request, 'home.html')