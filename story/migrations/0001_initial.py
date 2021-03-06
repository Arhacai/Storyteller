# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-03 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, unique=True)),
                ('text', tinymce.models.HTMLField(verbose_name='Content')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
