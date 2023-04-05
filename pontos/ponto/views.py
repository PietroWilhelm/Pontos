from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from usuarios.models import usuarios
from .models import ponto

# Create your views here.

def baterponto(request):
    pessoas = usuarios.objects.all().values()
    context = {
        'pessoas': pessoas,
    }
    if request.method == 'POST':
        pessoa = request.POST.get('usuario')

        usuario = usuarios.objects.get(id_usuarios=f'{pessoa}')
        
        novoponto = ponto(id_usuario=usuario)
        novoponto.save()
        
    return render(request, template_name='baterponto.html', context=context)

