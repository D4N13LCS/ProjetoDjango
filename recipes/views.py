from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def MyView(request):
    return HttpResponse('Que isso, pai!')

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Daniel'})