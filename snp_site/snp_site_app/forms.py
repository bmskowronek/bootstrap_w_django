from django import forms
from .models import Species
from django import forms

class SpeciesForm(forms.Form):
    selected_species_id = forms.IntegerField(widget=forms.HiddenInput())