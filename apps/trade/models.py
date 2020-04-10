from django.db import models

from user.models import Users
from goods.models import Goods


# Create your models here.


class Order(models.Model):
    STATUS_CHOICE = (
        (0, "未付款"),
        (1, "已付款"),
        (3, "未评价"),
        (4, "已评价"),
        (5, "退款中"),
        (6, "已退款"),
        (7, "未退款"),

    )

    EVALUATION_STATUS_CHOICE = (
    )

    user = models.ForeignKey(to=Users, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE, verbose_name='商品')
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    payment_status = models.IntegerField(choices=STATUS_CHOICE, default=0, verbose_name='状态')
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号")
    post_script = models.CharField(max_length=255, verbose_name="订单留言")
    order_mount = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="订单金额")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="订单生成时间")
    buy_time = models.DateTimeField(auto_now_add=True, verbose_name='购买时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ''.join(self.order_sn)
