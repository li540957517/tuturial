# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='screenshot',
            field=models.FileField(upload_to='uploads/', verbose_name='问题截图'),
        ),
    ]