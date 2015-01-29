# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20141209_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipo', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='noticia',
            name='resultas',
            field=models.ManyToManyField(to='app.Resulta', null=True),
            preserve_default=True,
        ),
    ]
