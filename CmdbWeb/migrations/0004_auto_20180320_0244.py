# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CmdbWeb', '0003_auto_20180320_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentdetail',
            name='disk',
            field=models.CharField(max_length=128, verbose_name='\u786c\u76d8\u5927\u5c0f'),
        ),
    ]
