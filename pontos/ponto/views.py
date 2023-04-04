from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def baterponto(request):
    return render(request, template_name='baterponto.html')
