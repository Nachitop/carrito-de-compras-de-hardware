# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.producto.models import Producto

# Create your models here.

class Proveedor(models.Model):
	id_proveedor=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	rfc=models.CharField(max_length=13,unique=True)
	tel1=PhoneNumberField()
	tel2=PhoneNumberField(null=True)
	cp=models.IntegerField()
	calle=models.CharField(max_length=30)
	numero=models.CharField(max_length=5)
	colonia=models.CharField(max_length=30)
	entre_calles=models.CharField(max_length=30)
	referencias_cercanas=models.CharField(max_length=30)

class Compra(models.Model):
	id_compra=models.AutoField(primary_key=True)
	id_proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	fecha_compra=models.DateField()

class DetalleCompra(models.Model):
	id_compra=models.ForeignKey(Compra,on_delete=models.CASCADE)
	id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
	cantidad=models.IntegerField()
	precio=models.FloatField()
	
