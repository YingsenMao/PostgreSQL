from django.conf.urls import url

from . import views

app_name = 'data'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^api/sum_by_sex_year', views.sum_by_sex_year, name='sum_by_sex_year'),
    url(r'^api/(?P<baby_name>[a-zA-Z]+)/sum_by_sex_year/$', views.name_sum_by_year, name='name_sum_by_year'),
]