# Generated by Django 2.0.3 on 2018-04-12 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=20)),
                ('phone', models.CharField(max_length=20)),
                ('addtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
