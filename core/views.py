from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'base.html'
    context = {
        'mensagem': 'Bem vindo ao site WEBFilmes'
    }
    return render(request, template_name, context)