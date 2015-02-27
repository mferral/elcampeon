#encoding:utf-8
from django import forms
from django.forms import Textarea
from app.models import Noticia,Publicidad
from nicedit.widgets import NicEditAdminWidget

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        widgets={
            "titulo":forms.TextInput(attrs={'required':'True','placeholder':'Titulo','class':'span12'}),
            "subtitulo":forms.TextInput(attrs={'required':'True','placeholder':'Subtitulo','class':'span12'}),
            "quienescribe":forms.TextInput(attrs={'required':'True','placeholder':'Quien Escribe?','class':'span12'}),
            #"contenido": Textarea(attrs={'cols': 80, 'rows': 4,'class':'span12'}),
            "contenido":NicEditAdminWidget(attrs={'cols': 80,'class':'span12'},                
                js_options={"buttonList": [
                    'save', 'bold', 'italic', 'underline', 'left', 'center',
                    'right', 'justify', 'ol', 'ul', 
                    #'fontSize',  # 'fontFamily',
                    #'fontFormat',
                    'indent', 'outdent', 'upload', 'link',
                    'unlink', 'forecolor', 'bgcolor']}
            ),
            "seccion":forms.Select(attrs={'required':'True'}),
            "tiponoticia":forms.Select(attrs={'required':'True'}),
            "imagen":forms.FileInput(attrs={'required':'True'}),
        } 

class PublicidadForm(forms.ModelForm):
    class Meta:
        model = Publicidad
        widgets={
            "piedefoto":forms.TextInput(attrs={'required':'True','placeholder':'Titulo','class':'span12'}),
            "url":forms.TextInput(attrs={'required':'True','placeholder':'URL','class':'span12'}),
            "imagen":forms.FileInput(attrs={'required':'True'}),
        }
    