# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0002_auto_20170726_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='desination',
            new_name='destination',
        ),
    ]
