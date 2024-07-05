from django.contrib import admin
from .models import Species, Chromosome, SNP

class ChromosomeInline(admin.TabularInline):
    model = Chromosome
    extra = 3  # Number of extra forms to show by default
    fields = ['name']  # Fields to display in the inline form

class SNPInline(admin.TabularInline):
    model = SNP
    extra = 3  # Number of extra forms to show by default

class SpeciesAdmin(admin.ModelAdmin):
    inlines = [ChromosomeInline]

class ChromosomeAdmin(admin.ModelAdmin):
    inlines = [SNPInline]

admin.site.register(Species, SpeciesAdmin)
admin.site.register(Chromosome, ChromosomeAdmin)
admin.site.register(SNP)