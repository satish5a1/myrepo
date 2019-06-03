# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=300)),
                ('date', models.DateTimeField(max_length=50)),
            ],
        ),
    ]