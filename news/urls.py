from django.urls import path
from .import views


urlpatterns = [
    path('', views.news_home, name = 'news_home'),
    path('news', views.create, name = 'create'),
]