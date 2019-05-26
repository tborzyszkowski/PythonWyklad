# Generated by Django 2.2.1 on 2019-05-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GraphMaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matrix', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(verbose_name='date added')),
                ('editCounter', models.IntegerField(default=0)),
                ('wrongCounter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GraphType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='graphs',
            name='graph_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GraphMaster.GraphType'),
        ),
    ]