# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 19:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zapisy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapisy',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zapisy',
            name='your_choice',
            field=models.CharField(choices=[('J', 'Modern jazz'), ('B', 'Modern balet'), ('A', 'Afro dance'), ('D', 'Break dance')], max_length=1, null=True),
        ),
    ]
