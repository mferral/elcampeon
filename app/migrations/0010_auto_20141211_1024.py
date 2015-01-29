# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20141211_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='resultas',
            field=models.ManyToManyField(to='app.Resulta', null=True, blank=True),
            preserve_default=True,
        ),
    ]
