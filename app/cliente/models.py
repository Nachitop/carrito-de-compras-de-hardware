# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from app.producto.models import Producto

# Create your models here.

class Cliente(models.Model):
	usuario=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	rfc=models.CharField(max_length=13,unique=True)
	tel1=PhoneNumberField()
	tel2=PhoneNumberField(blank=True, null=True)
	avatar=models.ImageField(upload_to='avatars', null=True, blank=True)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4}"
		return cadena.format(str(self.usuario.id),self.nombre,self.apellido,self.rfc,str(self.tel1),str(self.tel2))
	  
class DomicilioCliente(models.Model):
	id_domiciliocliente=models.AutoField(primary_key=True)
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
	cp=models.IntegerField()
	calle=models.CharField(max_length=30)
	numero=models.CharField(max_length=5)
	colonia=models.CharField(max_length=30)
	entre_calles=models.CharField(max_length=30)
	referencias_cercanas=models.CharField(max_length=30)

class Favorito(models.Model):
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
