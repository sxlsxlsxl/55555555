from django.contrib import admin
from goods import  models as goods_models
# Register your models here.
admin.site.register(goods_models.GoodsCategory)
admin.site.register(goods_models.Goods)
admin.site.register(goods_models.GoodsImages)