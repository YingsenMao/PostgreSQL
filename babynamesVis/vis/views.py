from .models import Babynames
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def index(request):
    return render(request, 'vis/graph.html')

def linear_reg(dt, year):
    timescale = 2016 - year
    df = pd.DataFrame(dt)[-timescale:]
    total = df['total'].values
    year = df['year'].values
    model = LinearRegression(fit_intercept=True)
    model.fit(year[:, np.newaxis], total)
    return model.coef_[0].tolist()

def name_sum_by_year(request, baby_name, year):
    data = Babynames.objects.filter(name = baby_name).values('year').annotate(total = Sum('n')).order_by('year')
    coeff = linear_reg(list(data), int(year))
    dt = {'coeff': coeff,
            'data': list(data)}
    return JsonResponse(dt)