# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-05-01 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
            ],
        ),
    ]