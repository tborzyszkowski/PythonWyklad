# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zajecia', '0007_auto_20180509_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zajecia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='zajecia/'),
        ),
    ]
