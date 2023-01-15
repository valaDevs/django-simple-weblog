from django.http import request
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')