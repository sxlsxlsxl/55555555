"""yishared URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
# from goods.urls import router as goods_router
import xadmin

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'xadmin/', xadmin.site.urls),
    url(r'api/(?P<version>[v1]+)/user/', include('user.urls')),
    url(r'api/(?P<version>[v1]+)/goods/', include('goods.urls')),
    url(r'api/(?P<version>[v1]+)/order/', include('trade.urls')),
    # url(r'api/(?P<version>[v1]+)/goods/', include(goods_router.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),


]
