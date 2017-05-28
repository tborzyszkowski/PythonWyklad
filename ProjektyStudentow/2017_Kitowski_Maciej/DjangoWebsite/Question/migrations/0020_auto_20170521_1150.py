# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0019_auto_20170521_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='ip',
            field=models.TextField(null=True, verbose_name=b'IP address', blank=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='useragent',
            field=models.TextField(null=True, verbose_name=b'User agent', blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='ip',
            field=models.TextField(null=True, verbose_name=b'IP address', blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='useragent',
            field=models.TextField(null=True, verbose_name=b'User agent', blank=True),
        ),
    ]
