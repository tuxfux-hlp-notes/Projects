# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-08 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20160808_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publihser',
            new_name='publisher',
        ),
    ]
