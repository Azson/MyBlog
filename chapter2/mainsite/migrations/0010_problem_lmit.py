# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_remove_problem_lmit'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='lmit',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
