from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters

# Create your views here.
from goods.serializes import GoodListSerializer, GoodImageSerializer, CategoryListSerializer
from goods.models import GoodsCategory, GoodsImages, Goods
from tools.pagination import MyPageNumberPagination


class GoodsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, filters.SearchFilter):
    queryset = Goods.objects.all()
    serializer_class = GoodListSerializer
    pagination_class = MyPageNumberPagination
    # 设置过滤器
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    # 设置自定义的过滤类
    # filterset_class = GoodsFilter

    # 指定搜索字段('=name':标示精准查找，'name':表示模糊匹配)
    search_fields = ['name', 'brief', 'goods_desc']

    # 指定排序字段(sold_num:销量)
    ordering_fields = ['sold_num', 'now_price']


class Categorylist(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = CategoryListSerializer


class CategoryGoods(ListModelMixin, GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodListSerializer
    pagination_class = MyPageNumberPagination

    def get_goods_queryset(self, pk):
        goods = self.queryset.filter(category_id=pk).all()
        return goods

    def list(self, request, *args, **kwargs):
        a = request.COOKIES
        print(a, 1111111111111111111111111111111111111111111)
        resp = {
            'code': 1,
            'msg': '请求成功'
        }
        pk = kwargs.get('pk')
        # print(pk, 111111111111)
        # self.get_queryset(pk)
        queryset = self.filter_queryset(self.get_goods_queryset(pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        resp['data'] = serializer.data
        return Response(resp)
