# from rest_framework.routers import DefaultRouter
#
# from goods.views import GoodsViewSet
#
# router = DefaultRouter()
# router.register(r'list',
#                 GoodsViewSet, basename='goodslist')
# router.register(r'category',
#                 GoodsViewSet, basename='goodslist')
#
from django.conf.urls import url, include
from django.urls import path
from goods.views import GoodsViewSet, GoodsImages, Categorylist,CategoryGoods

urlpatterns = [
    url(r'category/$', Categorylist.as_view({'get': 'list'}), name='goodlist'),
    url(r'category/(?P<pk>\d+)/$', CategoryGoods.as_view({'get': 'list'}), name='goodlist'),
    url(r'list/$', GoodsViewSet.as_view({'get': 'list'}), name='goodlist'),
    url(r'detail/(?P<pk>\d+)/$', GoodsViewSet.as_view({'get': 'retrieve'}), name='gooddetail'),
]
