# Generated by Django 2.2.1 on 2019-05-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_type_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='i_watched',
            field=models.BooleanField(default=False),
        ),
    ]
