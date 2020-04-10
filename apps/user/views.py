from http import cookies
from django.contrib.auth import login, logout
from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from user.models import Users
from django.http import JsonResponse
from rest_framework.views import APIView
from user.serializes import RegisterSerializer, UserInfoserializer

cookie = cookies.SimpleCookie()

''' token md5加密'''
import hashlib
import time


def md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


def pwd_md5(pwd):
    m = hashlib.md5(bytes(pwd, encoding='utf-8'))
    return m.hexdigest()


class Login(APIView):
    '''
    用户登录
    '''
    resp = {
        'status code': 1,
        'msg': '成功',
    }


    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            if data:
                username = ''.join(data.get('username'))
                password = ''.join(data.get('password'))

                if username and password:
                    user = Users.objects.filter(Q(username=username) | Q(mobile=username)).first()
                    if not user:
                        self.resp = {
                            'status code': -1,
                            'msg': '账号未注册'
                        }
                        return JsonResponse(self.resp)
                    new_password = pwd_md5(password)
                    if new_password != user.password:
                        self.resp = {
                            'status code': -1,
                            'msg': '密码错误'
                        }
                        return JsonResponse(self.resp)
                    # 为登陆用户创建token
                    token = md5(user.mobile)
                    # 存在就更新,不存在就创建
                    self.resp['token'] = token
                    # request.set_cookie('user', token, max_age=7 * 24 * 60 * 60)

                    login(request, user)

        except Exception as err:
            print(err)
            self.resp['state_code'] = 1002
            self.resp['msg'] = '请求异常'

        return JsonResponse(self.resp)


class Logout(APIView):
    '''
    退出登录
    '''
    resp = {
        'status code': 1,
        'msg': '成功',
    }

    def get(self, request, *args, **kwargs):
        try:
            logout(request)
            self.resp['msg'] = '已退出'
            return JsonResponse(self.resp)
        except Exception as err:
            self.resp['status code'] = -1
            self.resp['msg'] = '请求异常'
            return JsonResponse(self.resp)


class Register(CreateModelMixin, GenericViewSet):
    '''
    用户注册
    '''
    queryset = Users.objects.all()

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        resp = {
            'status code': 1,
            'msg': '成功'
        }
        # print(request.data)
        data = request.data.copy()
        pwd = data['password']
        new_password = pwd_md5(pwd)
        data['password'] = new_password
        serializer = self.get_serializer(data=data)
        # print(serializer,11111111111111111111)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            resp['data'] = serializer.data
            return Response(resp, status=status.HTTP_201_CREATED, headers=headers)
        else:
            resp['status code'] = -1
            resp['msg'] = '注册失败'
            resp['error'] = serializer.errors
        return Response(resp)


class SendCode(APIView):
    '''
    验证码
    '''


class ForgetPwd(APIView):
    '''
    忘记密码
    '''
    resp = {
        'status code': 1,
        'msg': '成功'
    }

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        if data:
            mobile = data['mobile']
            # code = data.get['code']
            password = data['password']
            password1 = data['password1']
            # if code is None:
            #         self.resp['status code'] = -1
            #         self.resp['msg'] = '参数错误'
            #         return JsonResponse(self.resp)
            if not mobile:
                self.resp['status code'] = -2
                self.resp['msg'] = '参数错误'
                return JsonResponse(self.resp)
            user = Users.objects.filter(mobile=mobile).first()
            if not user:
                self.resp['status code'] = -1
                self.resp['msg'] = '没有该用户'
                return JsonResponse(self.resp)

            if password != password1:
                self.resp['status code'] = -1
                self.resp['msg'] = '两次密码不一致'
                return JsonResponse(self.resp)
            user.password = password
            user.save()
            return JsonResponse(self.resp)


class UserInfoModelMixin(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    '''
    用户详情/修改
    '''
    queryset = Users.objects.all()
    serializer_class = UserInfoserializer
    resp = {
        'status code': 1,
        'msg': '成功'
    }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.resp['data'] = serializer.data
        return Response(self.resp, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(request.data, '111111111111111111')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():

            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            self.resp['data'] = serializer.data
            return Response(self.resp)
        else:
            self.resp['status code'] = -1
            self.resp['msg'] = '修改失败'
            self.resp['error'] = serializer.errors
            return Response(self.resp, status=status.HTTP_201_CREATED)
