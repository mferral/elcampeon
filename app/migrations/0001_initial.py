# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250)),
                ('subtitulo', models.CharField(max_length=250)),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to=b'fotos')),
                ('quienescribe', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoticiaSeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seccionprincipal', models.BooleanField(default=False)),
                ('resultados', models.BooleanField(default=False)),
                ('subseccion', models.CharField(max_length=50, blank=True)),
                ('noticia', models.ForeignKey(to='app.Noticia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'publicidad')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('piedefoto', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipo1', models.CharField(max_length=50)),
                ('resultado1', models.IntegerField()),
                ('equipo2', models.CharField(max_length=50)),
                ('resultado2', models.IntegerField()),
                ('noticia', models.ForeignKey(to='app.Noticia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoNoticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('usuario', models.CharField(unique=True, max_length=50)),
                ('contrasena', models.CharField(max_length=18)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='noticiaseccion',
            name='seccion',
            field=models.ForeignKey(to='app.Seccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noticia',
            name='tiponoticia',
            field=models.ForeignKey(to='app.TipoNoticia'),
            preserve_default=True,
        ),
    ]
