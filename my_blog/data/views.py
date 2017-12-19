from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Babynames2
#from django.template import loader
from django.http import JsonResponse
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render

def index(request):

    #firstFive = Babynames2.objects.only('name')[:1000]
    
    
    #context = {'firstFive': firstFive}

    #return render(request, 'data/data.html', context)
    return render(request, 'data/data_name.html')

def sum_by_sex_year(request):
    #data = Babynames2.objects.values('year', 'sex').annotate(total = Sum('n')).order_by('year')
    data = Babynames2.objects.values('year').annotate(total = Sum('n')).order_by('year')
    return JsonResponse(list(data), safe=False)


def name_sum_by_year(request, baby_name):
    data = Babynames2.objects.filter(name = baby_name).values('year').annotate(total = Sum('n')).order_by('year')
    return JsonResponse(list(data), safe=False)