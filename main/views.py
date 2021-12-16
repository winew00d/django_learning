from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def about1(request):
    return render(request, 'main/about.html')

def about2(request):
    return render(request, 'main/about.html')