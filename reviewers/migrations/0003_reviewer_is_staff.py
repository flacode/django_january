# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewers', '0002_auto_20160122_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
