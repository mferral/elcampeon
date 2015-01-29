# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141208_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='seccion',
            field=models.ForeignKey(default=0, to='app.Seccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='subseccion',
            field=models.CharField(default=0, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='tieneresultados',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
