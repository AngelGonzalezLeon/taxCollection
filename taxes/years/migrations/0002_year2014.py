# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('years', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year2014',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GeoName', models.CharField(max_length=200)),
                ('Year', models.CharField(max_length=200)),
                ('Total_Tax', models.CharField(max_length=200)),
                ('Property_Tax', models.CharField(max_length=200)),
                ('Sales_Tax', models.CharField(max_length=200)),
                ('License_Tax', models.CharField(max_length=200)),
                ('Income_Tax', models.CharField(max_length=200)),
                ('Other_Tax', models.CharField(max_length=200)),
            ],
        ),
    ]
