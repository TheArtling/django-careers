# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Title')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('job_description', django_markdown.models.MarkdownField(blank=True, verbose_name='Job Description')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
