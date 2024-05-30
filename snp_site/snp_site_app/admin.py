from django.contrib import admin
from .models import Species, Chromosome, SNP
admin.site.register(Species)
admin.site.register(Chromosome)
admin.site.register(SNP)
# Register your models here.
