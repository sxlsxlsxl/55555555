from django.conf.urls import url, include
from django.urls import path
from trade.views import OrderInfoViewSet

#
urlpatterns = [
    url(r'list/$', OrderInfoViewSet.as_view({'get': 'list', 'delete': 'destroy'}), name='goodlist'),
    url(r'info/(?P<pk>\d+)/$',
        OrderInfoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'post': 'create', 'delete': 'destroy'}),
        name='goodlist'),

]
