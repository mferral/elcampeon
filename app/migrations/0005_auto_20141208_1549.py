# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141208_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='seccion',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='subseccion',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='tieneresultados',
        ),
    ]
