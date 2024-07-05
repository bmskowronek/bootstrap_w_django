from django.urls import path
from django.shortcuts import redirect
from . import views


app_name = 'snps'

urlpatterns = [
    path('', lambda request: redirect('index/', permanent=True)),  
    path("index/", views.index, name="index"),
    path("snps/", views.snps, name="snps"),
    path('get_snps/', views.get_snps, name='get_snps'),
    path('snps/annotation/<int:snp_id>/', views.snp_annotation_detail, name='snp_annotation_detail'),
    path('download_csv/', views.download_snps_csv, name='download_snps_csv'),
]