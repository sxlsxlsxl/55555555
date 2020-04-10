from rest_framework import serializers

from goods.models import Goods, GoodsImages, GoodsCategory


class GoodImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = GoodsImages
        fields = ['image']


class GoodListSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    images = GoodImageSerializer(many=True)

    class Meta():
        model = Goods
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta():
        model = GoodsCategory
        fields = '__all__'


# class CategoryGoodsSerializer(serializers.ModelSerializer):
#     category = serializers.IntegerField()
#
#     class Meta():
#         model = Goods
