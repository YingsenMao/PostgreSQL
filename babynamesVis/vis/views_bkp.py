from django.http import HttpResponse
from .models import Babynames
from django.http import JsonResponse
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render

# rest framework
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from vis.serializers import BabyNameSerializer

# rest framework cbv
from rest_framework.generics import ListAPIView

def index(request):

    #firstFive = Babynames2.objects.only('name')[:1000]
    
    
    #context = {'firstFive': firstFive}

    #return render(request, 'data/data.html', context)
    return render(request, 'vis/graph.html')


def name_sum_by_year(request, baby_name):
    data = Babynames.objects.filter(name = baby_name).values('year').annotate(total = Sum('n')).order_by('year')
    return JsonResponse(list(data), safe=False)


'''
@csrf_exempt
def babyname_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        babynames = Babynames.objects.filter(name = 'Jay')
        serializer = BabyNameSerializer(babynames, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BabyNameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
'''


@csrf_exempt
def babyname_detail(request, baby_name):
    if request.method == 'GET':
        data = Babynames.objects.filter(name = baby_name).values('year').annotate(n = Sum('n')).order_by('year')
        serializer = BabyNameSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    """
    Retrieve, update or delete a code snippet.
  
    try:
        babyname = Babynames.objects.get(pk=pk)
    except Babynames.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BabyNameSerializer(babyname)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    """

class Babyname_list_2(ListAPIView):
    queryset = Babynames.objects.all()
    serializer_class = BabyNameSerializer
    def get_queryset(self):
        return self.queryset.filter(name = self.kwargs.get('baby_name')).values('year').annotate(n = Sum('n')).order_by('year')