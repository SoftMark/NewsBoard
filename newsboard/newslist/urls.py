from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Articles
from django.urls import path
from . import views

urlpatterns = [
    path('',
        ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
        template_name="home/index.html")),
    path('create_post/', views.post_create, name='create_post'),
]
