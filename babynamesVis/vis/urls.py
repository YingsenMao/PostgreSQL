from django.conf.urls import url

from . import views

app_name = 'vis'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<baby_name>[a-zA-Z]+)/(?P<year>[0-9]+)/$', views.name_sum_by_year, name='babyname_1'),
    #url(r'^api/v2/(?P<baby_name>[a-zA-Z]+)/$', views.babyname_detail, name='babyname_2'),
    #url(r'^api/v3/(?P<baby_name>[a-zA-Z]+)/$', views.Babyname_list_2.as_view(), name='babyname_3'),

    #url(r'^api/(?P<baby_name>[a-zA-Z]+)/$', views.linear_reg, name='coeff'),
]