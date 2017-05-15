# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busdata', '0005_registro_fonte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=100)),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'autor',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='registro',
            name='autor',
            field=models.ForeignKey(default=None, blank=True, to='busdata.Autor', null=True),
        ),
    ]
