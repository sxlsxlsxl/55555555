from django.db import models

from extra_apps.DjangoUeditor.models import UEditorField
from user.models import Users



class GoodsCategory(models.Model):
    """
    商品类别
    """

    name = models.CharField(default="", max_length=32, verbose_name="类别名", help_text="类别名")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    is_tab = models.BooleanField(default=False, verbose_name="是否展示", help_text="是否展示")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    STATUS_CHOICE = (
        (1, "上架"),
        (0, "下架")
    )

    POPULAR_CHOICE = (
        (1, "是"),
        (0, "否")
    )

    name = models.CharField(max_length=255, null=False, verbose_name='商品名')
    front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    user = models.IntegerField(default=1, verbose_name='商家')
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    original_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='原价')
    now_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='现价')
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    stock = models.IntegerField(default=0, verbose_name='库存')
    up_time = models.DateTimeField(auto_now=True, verbose_name='上架时间')
    status = models.IntegerField(choices=STATUS_CHOICE, default=0, verbose_name='状态')
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    area = models.CharField(max_length=255, null=True, default=None, verbose_name='商品地区')
    is_new = models.BooleanField(default=True, verbose_name="是否新品")
    popular = models.IntegerField(choices=POPULAR_CHOICE, default=0, verbose_name='是否热门')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImages(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="goods/", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
