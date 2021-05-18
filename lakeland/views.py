from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def rtis(request):
    return render(request, 'rtis.html')

def ds(request):
    return render(request, 'ds.html')

def ycs(request):
    return render(request, 'ycs.html')