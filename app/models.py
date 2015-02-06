#encoding:utf-8
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    usuario=models.CharField(max_length=50,unique=True)
    contrasena=models.CharField(max_length=18)
    activo=models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombre

class Seccion(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion

class TipoNoticia(models.Model):
    descripcion=models.CharField(max_length=30)
    def __unicode__(self):
        return self.descripcion                

class Publicidad(models.Model):
	imagen = models.ImageField(upload_to='publicidad')        
	fecha=models.DateTimeField(auto_now_add=True,editable=False)  
	piedefoto=models.CharField(max_length=250)
	url=models.CharField(max_length=250)
	def __unicode__(self):
		return self.piedefoto 

class Resulta(models.Model):	
	equipo1=models.CharField(max_length=50,null=True)
	resultado1=models.IntegerField()
	equipo2=models.CharField(max_length=50,null=True)
	resultado2=models.IntegerField()
	def __unicode__(self):
		return self.equipo1	

class Noticia(models.Model):
	titulo=models.CharField(max_length=250)
	subtitulo=models.CharField(max_length=250)
	contenido=models.TextField(blank=False)
	fecha=models.DateTimeField(auto_now_add=True,editable=False) 
	imagen = models.ImageField(upload_to='fotos')  
	quienescribe=models.CharField(max_length=200)
	tieneresultados=models.BooleanField(default=False)
	subseccion=models.CharField(max_length=50,blank=True,null=True)	
	seccion=models.ForeignKey(Seccion,null=True)	
	tiponoticia=models.ForeignKey(TipoNoticia,null=True)	
	resultas = models.ManyToManyField(Resulta, null=True,blank=True)
	def __unicode__(self):
		return self.titulo

class NoticiaSeccion(models.Model):
	noticia=models.ForeignKey(Noticia)
	seccion=models.ForeignKey(Seccion)	
	def __unicode__(self):
		return self.noticia.titulo
