# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_job', models.TextField()),
                ('created_date', models.DateTimeField(editable=False, default=datetime.datetime(2015, 10, 15, 15, 0, 39, 27128))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=200)),
                ('join_date', models.DateTimeField(editable=False, default=datetime.datetime(2015, 10, 15, 15, 0, 39, 26584))),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(to='data.User'),
        ),
    ]
