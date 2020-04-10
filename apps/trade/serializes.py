import time
import random
from rest_framework import serializers
from trade.models import Order
from goods.serializes import GoodListSerializer


class OrderSerializer(serializers.ModelSerializer):
    goods = GoodListSerializer()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    buy_time = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S',
        read_only=True
    )
    add_time = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S',
        read_only=True
    )
    post_script = serializers.CharField(
        required=False
    )
    order_sn = serializers.CharField(
        read_only=True
    )
    trade_no = serializers.CharField(
        read_only=True
    )
    payment_status = serializers.CharField(
        read_only=True
    )

    def create_order_sn(self):
        now_time = time.strftime('%Y%m%d%H%M%S')
        str_list = list(now_time)

        for i in range(4):
            random_ins = str(random.randint(0, 9))
            random_index = random.randint(0, 9)

            print('random_ins-----', random_ins)
            print('random_index-----', random_index)
            str_list.insert(random_index, random_ins)
        str_ins = ''.join(str_list)

        order_sn = '{nowtime}{userid}'.format(nowtime=str_ins, userid=self.context['request'].user.id)
        return order_sn

    def validate(self, attrs):
        attrs['order_sn'] = self.create_order_sn()
        return attrs

    class Meta():
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = GoodListSerializer(many=True)

    class Meta():
        model = Order
        field = '__all__'
