# This file is not generate within project creation. 

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return  render(request, 'home.html')