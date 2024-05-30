from django.urls import path
from django.shortcuts import render
from . import views

def index(request):
    #uses template
    return render(request, "snp_site_app/index.html")

def snps(request):
    #uses template
    return render(request, "snp_site_app/snps.html")