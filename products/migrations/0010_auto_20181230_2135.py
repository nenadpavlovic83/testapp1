# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-30 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20181230_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='test', unique=True),
        ),
    ]
