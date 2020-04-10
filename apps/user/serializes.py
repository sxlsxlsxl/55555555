import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import Users
from yishared.settings import REGEX_MOBILE


class RegisterSerializer(serializers.ModelSerializer):
    # add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    mobile = serializers.CharField(
        max_length=11,
        validators=[
            # 判断用户名是否唯一
            UniqueValidator(
                queryset=Users.objects.all(),
                message='该手机号已存在'
            )
        ],
        error_messages={
            'max_length': '手机号长度问题'
        }
    )
    username = serializers.CharField(
        required=True,
        allow_blank=True,
        validators=[
            # 判断用户名是否唯一
            UniqueValidator(
                queryset=Users.objects.all(),
                message='该用户已存在'
            )
        ],
        help_text='用户名',
        label='用户名'

    )
    password = serializers.CharField(
        min_length=6,
        style={'input_type': 'password'},
        label='密码',
        write_only=True,
        error_messages={
            'max_length':'密码过长',
            'mix_length':'密码过短',
        }

    )

    # birthday = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta():
        model = Users
        fields = ['username', 'password', 'mobile']

    def validate_password(self, data):
        from rest_framework.exceptions import ValidationError
        if len(data) >= 6:
            return data
        else:
            raise ValidationError('密码长度错误')

    # def validate_mobile(self, attrs):


class UserInfoserializer(serializers.ModelSerializer):
    birthday = serializers.DateField(
        format='%Y-%m-%d',

    )

    class Meta():
        model = Users
        fields = ['mobile','username','gender','birthday','avatar','experience','grade']
