# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 08:59
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0017_remove_blog_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='内容')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]