from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'snps'

urlpatterns = [
    path('', lambda request: redirect('index/', permanent=True)),  
    path("index/", views.index, name="index"),
    path("snps/", views.snps, name="snps"),
]