# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from app.cliente.forms import *
from app.cliente.models import *
from django.contrib.auth.models import User
from app.tienda.views import *

# Create your views here.
def registro_view(request):
	if request.method=="POST":
		form=RegistroForm(request.POST)
		if form.is_valid():
			form.save()
			usuario=User.objects.get(username=request.POST.get('username'))
			Cliente.objects.create(usuario=usuario,nombre=request.POST.get('first_name'),apellido=request.POST.get('last_name'),rfc=usuario.id,tel1="+41524204242",tel2=+41524204242)
			return redirect('cliente:perfil')
	else:
		form=RegistroForm
	return render(request, 'registrarse/registro.html',{'form':form})

def perfil_view(request):
	categorias=Categoria.objects.all().order_by("categoria")
	cliente=Cliente.objects.get(usuario=request.user.id)
	contexto= {'categorias': categorias, 'cliente':cliente}
	return render(request,'registrarse/perfil.html',contexto)