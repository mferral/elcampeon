# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20141211_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultados',
            name='noticia',
        ),
        migrations.DeleteModel(
            name='Resultados',
        ),
    ]
