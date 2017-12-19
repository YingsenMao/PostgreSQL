# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-11 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Babynames2',
            fields=[
                ('year', models.FloatField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
                ('prop', models.FloatField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'babynames2',
                'managed': False,
            },
        ),
    ]
