# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('time', models.DateField()),
                ('email', models.TextField()),
                ('amount', models.TextField()),
            ],
        ),
    ]
