# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0012_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainsite.User'),
        ),
    ]
