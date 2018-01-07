# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-19 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Babynames',
            fields=[
                ('year', models.IntegerField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('n', models.IntegerField(blank=True, null=True)),
                ('prop', models.FloatField(blank=True, null=True)),
                ('name_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'babynames',
                'managed': False,
            },
        ),
    ]
