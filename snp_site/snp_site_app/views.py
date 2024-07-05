from django.urls import path
from django.shortcuts import render
from .models import Species, Chromosome, SNP
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import SpeciesForm 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv

def index(request):

    num_snps =  SNP.objects.count 
    num_samples = Chromosome.objects.count
    num_species = Species.objects.count
    context = {"num_snps": num_snps, "num_samples": num_samples, "num_species": num_species}
    return render(request, "snp_site_app/index.html", context)

def snps(request):
    species_list = Species.objects.order_by("-name")
    context = {"species_list": species_list}
    context["chosen_species"] = None
    return render(request, 'snp_site_app/snps.html', context)

def get_snps(request):
    species_list = Species.objects.order_by("-name")
    maf_min = request.GET.get('maf_min', request.POST.get('maf_min'))
    maf_max = request.GET.get('maf_max', request.POST.get('maf_max'))
    region = request.GET.get('region', request.POST.get('region'))
    context = {"species_list": species_list, "maf_min": maf_min, "maf_max": maf_max, "region": region}
    
    if request.method == 'POST':
        form = SpeciesForm(request.POST)
        if form.is_valid():
            selected_species_id = form.cleaned_data['selected_species_id']
            species = get_object_or_404(Species, id=selected_species_id)
            snps = SNP.objects.filter(chromosome__species=species)
            if region:
                snps = snps.filter(chromosome__name=region)
            if maf_min:
                snps = snps.filter(maf__gte=float(maf_min))
            if maf_max:
                snps = snps.filter(maf__lte=float(maf_max))
            # Pagination
            paginator = Paginator(snps, 3)  # Show 3 SNPs per page
            page = request.GET.get('page')
            try:
                snp_list = paginator.page(page)
            except PageNotAnInteger:
                snp_list = paginator.page(1)
            except EmptyPage:
                snp_list = paginator.page(paginator.num_pages)

            context['chosen_species'] = species
            context['snp_list'] = snp_list
            context['selected_species_id'] = selected_species_id
        context['form'] = form
    else:
        selected_species_id = request.GET.get('selected_species_id', '')
        if selected_species_id:
            species = get_object_or_404(Species, id=selected_species_id)
            snps = SNP.objects.filter(chromosome__species=species)
            if region:
                snps = snps.filter(chromosome__name=region)
            if maf_min:
                snps = snps.filter(maf__gte=float(maf_min))
            if maf_max:
                snps = snps.filter(maf__lte=float(maf_max))
            # Pagination
            paginator = Paginator(snps, 3)  # Show 3 SNPs per page
            page = request.GET.get('page')
            try:
                snp_list = paginator.page(page)
            except PageNotAnInteger:
                snp_list = paginator.page(1)
            except EmptyPage:
                snp_list = paginator.page(paginator.num_pages)

            context['chosen_species'] = species
            context['snp_list'] = snp_list

        context['selected_species_id'] = selected_species_id
        context['form'] = SpeciesForm()

    return render(request, 'snp_site_app/snps.html', context)


def snp_annotation_detail(request, snp_id):
    snp = get_object_or_404(SNP, id=snp_id)
    return render(request, 'snp_site_app/snp_annotation_detail.html', {'snp': snp})

def download_snps_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="snps.csv"'

    writer = csv.writer(response)
    writer.writerow(['Chromosome', 'Position', 'REF allele', 'ALT allele', 'MAF'])

    snps = SNP.objects.all()  # Adjust the query to filter SNPs as required
    for snp in snps:
        writer.writerow([snp.chromosome.name, snp.position, snp.ref_allele, snp.alt_allele, snp.maf])

    return response