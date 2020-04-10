from django.conf.urls import url, include
from django.urls import path
from user.views import Login, Logout, Register, ForgetPwd, UserInfoModelMixin

urlpatterns = [
    url(r'login/$', Login.as_view(), name='login'),
    url(r'logout/$', Logout.as_view(), name='login'),
    url(r'register/$', Register.as_view({'post': 'create'}), name='register'),
    url(r'forget/$', ForgetPwd.as_view(), name='forget'),
    url(r'info/(?P<pk>\d+)/$', UserInfoModelMixin.as_view({'get': 'retrieve', 'put': 'update'}), name='info'),

]
