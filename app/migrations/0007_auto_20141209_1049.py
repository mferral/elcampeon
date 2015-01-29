# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20141209_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='seccion',
            field=models.ForeignKey(to='app.Seccion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noticia',
            name='tiponoticia',
            field=models.ForeignKey(to='app.TipoNoticia', null=True),
            preserve_default=True,
        ),
    ]
