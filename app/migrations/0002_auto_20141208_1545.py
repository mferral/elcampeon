# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticiaseccion',
            name='resultados',
        ),
        migrations.RemoveField(
            model_name='noticiaseccion',
            name='seccionprincipal',
        ),
        migrations.RemoveField(
            model_name='noticiaseccion',
            name='subseccion',
        ),
        migrations.AddField(
            model_name='noticia',
            name='seccion',
            field=models.ForeignKey(default=datetime.datetime(2014, 12, 8, 21, 45, 20, 489351, tzinfo=utc), to='app.Seccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='subseccion',
            field=models.CharField(default=datetime.datetime(2014, 12, 8, 21, 45, 30, 712538, tzinfo=utc), max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='tieneresultados',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
