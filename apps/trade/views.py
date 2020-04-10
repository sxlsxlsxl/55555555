from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from tools.MyMiddleware import MyMiddleware
from tools.premissions import IsOwnerOrReadOnly
from trade.models import Order
from trade.serializes import OrderSerializer, OrderDetailSerializer


class OrderInfoViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,ListModelMixin,GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        else:
            return OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).all()

