# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from app.models import Usuario,Noticia,Seccion,NoticiaSeccion,Resulta
from django.http import HttpResponse
from app.forms import NoticiaForm
import datetime
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
NOTICIAS_PAGINA=4

def home(request):
	secciones=Seccion.objects.all()	
	tercios=Noticia.objects.all().order_by('-fecha')[:3]
	banners=Noticia.objects.filter(tieneresultados=True).filter(tiponoticia__id=3).order_by('-fecha')[:3]
	estelar=Noticia.objects.filter(tiponoticia__id=2).order_by('-fecha').first()
	entrevista=Noticia.objects.filter(seccion__id=5).order_by('-fecha').first()
	correcaminos=Noticia.objects.filter(seccion__id=2).order_by('-fecha').first()
	salud=Noticia.objects.filter(seccion__id=4).order_by('-fecha').first()
	cultura=Noticia.objects.filter(seccion__id=3).order_by('-fecha').first()
	poster=Noticia.objects.all().order_by('?').first()
	noticias_todas=Noticia.objects.all().order_by('-fecha')
	paginator = Paginator(noticias_todas, NOTICIAS_PAGINA)	
	total_paginas=paginator.num_pages
	return render(request,'index.html',{'secciones':secciones,'tercios':tercios,'total_paginas':total_paginas,\
										'estelar':estelar,'entrevista':entrevista,'salud':salud,\
										'correcaminos':correcaminos,'cultura':cultura,'banners':banners,'poster':poster})

def login(request):
    request.session.clear()
    request.session.flush()
    return render(request,'administracion/login.html')

def frmnota(request):
	id_=None
	noticia=None
	if request.GET:
		id_=request.GET['id']
		noticia=Noticia.objects.get(pk=id_)
		formulario=NoticiaForm(instance=noticia)
	else:
		formulario=NoticiaForm()
	return render(request,'administracion/frmnota.html',{'formulario':formulario,'id':id_,'noticia':noticia})	

def noticias_principal(request,idpagina):
	noticias_todas=Noticia.objects.all().order_by('-fecha')
	paginator = Paginator(noticias_todas, NOTICIAS_PAGINA)
	todas = paginator.page(idpagina)
	return render(request,'noticias.html',{'todas':todas})		

def secciones_pagina(request,idseccion,idpagina):
	principal=Noticia.objects.filter(seccion__id=idseccion).order_by('-fecha').first()
	otras=NoticiaSeccion.objects.filter(seccion__id=idseccion).values_list('noticia__id')
	noticias_pagina=Noticia.objects.exclude(pk=principal.id).filter(Q(seccion__id=idseccion) | Q(pk__in=otras)).order_by('-fecha')
	paginator = Paginator(noticias_pagina, NOTICIAS_PAGINA)
	noticias = paginator.page(idpagina)
	return render(request,'seccion_noticias.html',{'noticias':noticias})	

def seccion(request,idseccion):		
	secciones=Seccion.objects.all()
	principal=Noticia.objects.filter(seccion__id=idseccion).order_by('-fecha').first()
	otras=NoticiaSeccion.objects.filter(seccion__id=idseccion).values_list('noticia__id')
	noticias=Noticia.objects.exclude(pk=principal.id).filter(Q(seccion__id=idseccion) | Q(pk__in=otras)).order_by('-fecha')
	paginator = Paginator(noticias, NOTICIAS_PAGINA)
	total_paginas=paginator.num_pages
	#noticias=Noticia.objects.exclude(pk=principal.id).filter(Q(seccion__id=idseccion)).order_by('-fecha')	
	return render(request,'seccion.html',{'total_paginas':total_paginas,'secciones':secciones,'principal':principal,'idseccion':idseccion})

def noticias(request):		
	secciones=Seccion.objects.all()
	return render(request,'administracion/template.html',{'secciones':secciones})

def entrada(request,identrada):		
	secciones=Seccion.objects.all()
	noticia=Noticia.objects.get(pk=identrada)
	return render(request,'entrada.html',{'secciones':secciones,'noticia':noticia})

def otras_secciones(request,idseccion):			
	secs=Seccion.objects.exclude(pk=idseccion)
	secciones=[]
	for sec in secs:
		item={}
		item['seccion']=sec			
		if request.GET:
			idnoticia=request.GET['id']
			noticia_seccion=NoticiaSeccion.objects.filter(noticia__id=idnoticia)		
			for nc in noticia_seccion:								
				if(sec.id==nc.seccion.id):
					item['check']=True
		secciones.append(item)	
	return render(request,'administracion/otras_secciones.html',{'secciones':secciones})

def tabla_noticias(request,palabra):
	fechaini=datetime.datetime.now()
	fechafin=datetime.datetime.now()
	tiempoini=datetime.time.min
	tiempofin=datetime.time.max
	fecha_inicial=datetime.datetime.combine(fechaini,tiempoini)
	fecha_final=datetime.datetime.combine(fechafin,tiempofin)		
	if palabra:
		noticias=Noticia.objects.filter(titulo__icontains=palabra)
	else:
		noticias=Noticia.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final))
	return render(request,'administracion/tabla_noticias.html',{'noticias':noticias})

def validar(request):
    request.session.clear()
    request.session.flush()
    if request.POST:
        try:
            u=Usuario.objects.get(usuario=request.POST['usuario'])
            if u.contrasena == request.POST['contrasena']:
                if u.activo == False:
                    redirect('/acceso/')
                else:
                    request.session['nombre']=(u.nombre).title()
                    request.session['idusuario']=u.id                                     
                    return redirect('/noticias/')    
            else:
                return HttpResponse(u'La contraseña no coincide')
        except Usuario.DoesNotExist:
            return redirect('/acceso')
    return redirect('/acceso')

def noticia_save(request):
    if request.POST:
        #id_=int(request.POST['id']) 
        id_=request.POST['id']
        if id_!= 'None':
        	id_=int(request.POST['id'])
        	noticia=Noticia.objects.get(pk=id_)
        	formulario = NoticiaForm(request.POST,request.FILES,instance=noticia)
        else:
        	formulario = NoticiaForm(request.POST,request.FILES)
        if formulario.is_valid():
        	noticia=formulario.save()  
        	NoticiaSeccion.objects.filter(noticia__id=id_).delete()
        	try:
        		noticia.resultas.objects.all().delete()
        	except:
        		print 'error'
        	if len(request.POST.getlist('mas_secciones')) > 0:
        		for seccion in request.POST.getlist('mas_secciones'):      			
        			NoticiaSeccion.objects.create(noticia_id=noticia.pk,seccion_id=seccion)
        	pregunta=int(request.POST['pregunta'])	
        	if pregunta==1:
        		equipo1=request.POST['equipo1']        		
        		resultado1=request.POST['resultado1']
        		equipo2=request.POST['equipo2']	
        		resultado2=request.POST['resultado2']        		
        		resulta=Resulta.objects.create(equipo1=equipo1,resultado1=resultado1,equipo2=equipo2,resultado2=resultado2)
        		noticia.resultas.add(resulta)
        		noticia.tieneresultados=True
        		noticia.save()        		
        
   		#if len(request.POST.getlist('mas_secciones')) > 0:            
        #    for seccion in request.POST.getlist('mas_secciones'): 
        #    	print  seccion                  
    return redirect('/noticias/')    