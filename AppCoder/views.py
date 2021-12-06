from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def familiareslist(request):
    return render(request, 'familiareslist.html')

def inicio(request):
    return render(request, 'inicio.html')
