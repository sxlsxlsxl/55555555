
from django.db import models



class Users(models.Model):

    '''
    用户基本信息
    '''

    GENDER_CHOICES = (
        (1, '男'),
        (0, '女')
    )

    username = models.CharField(max_length=150,unique=True, null=False, verbose_name='用户')
    password = models.CharField(max_length=255, null=False, verbose_name='密码')
    gender = models.IntegerField(null=False, choices=GENDER_CHOICES, default=1, verbose_name='性别')
    mobile = models.CharField(max_length=11,blank=True, verbose_name='手机')
    # email = models.CharField(max_length=128, blank=True, verbose_name='邮箱')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    avatar = models.URLField(max_length=255,verbose_name='头像')
    experience = models.IntegerField(default=0, verbose_name='经验')
    grade = models.IntegerField(default=0, verbose_name='等级')
    first_login = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_login = models.DateTimeField(auto_now=True, verbose_name='最后登录时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Assets(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE, verbose_name='用户')
    money = models.DecimalField( max_digits=20, decimal_places=2,verbose_name='资产')
    class Meta:
        verbose_name = '资产'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

