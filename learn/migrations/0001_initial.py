# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('email', models.EmailField(max_length=100, verbose_name='邮箱')),
                ('mobile', models.CharField(max_length=20, verbose_name='手机')),
            ],
        ),
    ]
