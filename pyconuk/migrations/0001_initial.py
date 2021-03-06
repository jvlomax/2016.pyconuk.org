# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_format', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('callout_big_1', models.CharField(max_length=255)),
                ('callout_big_2', models.CharField(max_length=255)),
                ('callout_small', models.CharField(max_length=255)),
                ('tito_required', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Redirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('new_url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
