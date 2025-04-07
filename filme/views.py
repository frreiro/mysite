from django.shortcuts import render, redirect
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
    print(request.method)
    if request.method == 'POST':
        form = FilmesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_filmes')
    else:        
        template_name = 'new_filmes.html'
        form = FilmesForm()
        context = {
            'form': form,
            'mensagem': 'Novo Filme'
        }
        return render(request, template_name, context)