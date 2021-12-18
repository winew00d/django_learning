from django.shortcuts import render

from news.models import Articles

# Create your views here.
def news_home(request):
    news = Articles.objects.all()
    return render (request, 'news/news_home.html', {'news': news})

def create(request):
    return render (request, 'news/create')