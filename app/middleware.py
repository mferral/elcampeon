from django.shortcuts import redirect

class Evalua:

	def process_view(self, request, view_func, view_args, view_kwargs):
		print request.path
		if 'nombre' not in request.session and '/acceso/' not in request.path and '/validar/' not in request.path and request.path!='/' :
			print 'fallo en el middleware'
			return redirect('/acceso')