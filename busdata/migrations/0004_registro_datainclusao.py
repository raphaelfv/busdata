# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-25 13:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('busdata', '0003_auto_20170325_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='dataInclusao',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2017, 3, 25, 13, 57, 53, 808786, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
