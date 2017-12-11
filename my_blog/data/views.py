from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Babynames2
#from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):

    firstFive = Babynames2.objects.only('name')[:1000]
    
    context = {'firstFive': firstFive}

    return render(request, 'data/data.html', context)