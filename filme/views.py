from django.shortcuts import render
from .models import Filmes
from .forms import FilmesForm
# Create your views here.
def list_filmes(request):
    filmes = Filmes.objects.all()
    template_name = 'list_filmes.html'
    context = {
         'filmes': filmes,
         'mensagem': 'Esses sao os filmes'
         }
    return render(request, template_name, context)

def new_filmes(request):
    template_name = 'new_filmes.html'
    form = FilmesForm()
    context = {
        'form': form,
        'mensagem': 'Novo Filme'
    }
    return render(request, template_name, context)