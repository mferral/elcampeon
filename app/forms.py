#encoding:utf-8
from django import forms
from django.forms import Textarea
from app.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        widgets={
            "titulo":forms.TextInput(attrs={'required':'True','placeholder':'Titulo','class':'span12'}),
            "subtitulo":forms.TextInput(attrs={'required':'True','placeholder':'Subtitulo','class':'span12'}),
            "quienescribe":forms.TextInput(attrs={'required':'True','placeholder':'Quien Escribe?','class':'span12'}),
            "contenido": Textarea(attrs={'cols': 80, 'rows': 4,'class':'span12'}),
            "seccion":forms.Select(attrs={'required':'True'}),
            "tiponoticia":forms.Select(attrs={'required':'True'}),
            "imagen":forms.FileInput(attrs={'required':'True'}),
        } 
    