from django.contrib import admin
from django.urls import path
from .views import ArticleList

app_name = 'blog'


urlpatterns = [
    path('',ArticleList.as_view(), name='article-list')
]