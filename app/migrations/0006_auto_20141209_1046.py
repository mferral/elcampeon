# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141208_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='tiponoticia',
        ),
        migrations.AddField(
            model_name='noticia',
            name='subseccion',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noticia',
            name='tieneresultados',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
