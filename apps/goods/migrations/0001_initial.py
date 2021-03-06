# Generated by Django 2.1 on 2020-04-09 01:16

from django.db import migrations, models
import django.db.models.deletion
import extra_apps.DjangoUeditor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='商品名')),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
                ('brief', models.TextField(max_length=500, verbose_name='商品简短描述')),
                ('user', models.IntegerField(default=1, verbose_name='商家')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='商品唯一货号')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='原价')),
                ('now_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='现价')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='商品销售量')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('up_time', models.DateTimeField(auto_now=True, verbose_name='上架时间')),
                ('status', models.IntegerField(choices=[(1, '上架'), (0, '下架')], default=0, verbose_name='状态')),
                ('goods_desc', extra_apps.DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('area', models.CharField(default=None, max_length=255, null=True, verbose_name='商品地区')),
                ('is_new', models.BooleanField(default=True, verbose_name='是否新品')),
                ('popular', models.IntegerField(choices=[(1, '是'), (0, '否')], default=0, verbose_name='是否热门')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品表',
                'verbose_name_plural': '商品表',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=32, verbose_name='类别名')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='GoodsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods/', verbose_name='图片')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
