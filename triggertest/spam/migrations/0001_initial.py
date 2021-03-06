# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 20:58
from __future__ import unicode_literals

import concurrency.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eggs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.TriggerVersionField(default=1, help_text='record revision number')),
                ('field', models.CharField(default='eggs', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Spam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.TriggerVersionField(default=1, help_text='record revision number')),
                ('field', models.CharField(default='spam', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
