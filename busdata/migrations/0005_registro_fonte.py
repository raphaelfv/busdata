# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busdata', '0004_registro_datainclusao'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='fonte',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
