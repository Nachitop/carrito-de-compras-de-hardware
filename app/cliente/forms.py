# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app.cliente.models import *

class RegistroForm(UserCreationForm):
	first_name=forms.CharField(max_length=50,required=True)
	last_name=forms.CharField(max_length=50,required=True)
	email=forms.EmailField(required=True)

	class Meta:
		model= User
		fields =[
			'username',
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
			]
		labels={
		 	'username': 'Nombre de usuario',
		 	'email': 'Email',
		 	'first_name': 'Nombres',
		 	'last_name': 'Apellidos',
		 	'password1': 'Contraseña',
		 	'password2': 'Confirmar contraseña',
		 	}
		# widgets={
		# 	'username':  forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Username'}),
		# 	'email': forms.TextInput(attrs={'class':'form-control','type':'text', 'placeholder':'Email'}),
		# 	'first_name': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Nombres'}),
		# 	'last_name': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Apellidos'}),
		# 	'password1': forms.TextInput(attrs={'type':'password', 'class':'form-control', 'placeholder':'Contraseña'}),
		# 	'password2': forms.TextInput(attrs={'type':'password', 'class':'form-control', 'placeholder':'Confirmar contraseña'}),
		# 	}