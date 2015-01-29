# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20141211_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resulta',
            name='equipo',
        ),
        migrations.AddField(
            model_name='resulta',
            name='equipo1',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resulta',
            name='equipo2',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resulta',
            name='resultado1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resulta',
            name='resultado2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
