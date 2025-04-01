from django import forms
from .models import Filmes

class FilmesForm(forms.ModelForm):
    class Meta:
        model = Filmes
        fields =  "__all__"