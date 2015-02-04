from django.shortcuts import redirect

class Evalua:

	def process_view(self, request, view_func, view_args, view_kwargs):
		print request.path
		if 'nombre' not in request.session and '/acceso/' not in request.path and '/validar/' not in request.path and request.path!='/' :
			if '/noticias_principal/' not in request.path and '/seccion/' not in request.path :
				if '/seccion_noticias/' not in request.path and '/entrada/' not in request.path and '/media/' not in request.path :
					print 'fallo en el middleware'
					return redirect('/acceso')
