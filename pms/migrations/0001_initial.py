# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-30 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类型名称')),
                ('description', models.CharField(max_length=100, verbose_name='备注说明')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('quantity_per_unit', models.CharField(max_length=50, verbose_name='单位数量')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('units_in_stock', models.IntegerField(default=0, verbose_name='库存数量')),
                ('discontinued', models.BooleanField(default=False, verbose_name='停产')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新')),
                ('posted_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pms.Category')),
            ],
            options={
                'ordering': ['-unit_price'],
            },
        ),
    ]
