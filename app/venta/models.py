# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from app.producto.models import Producto
from phonenumber_field.modelfields import PhoneNumberField
from app.cliente.models import Cliente

# Create your models here.

class EstadoVenta(models.Model):
	id_estado_venta=models.AutoField(primary_key=True)
	estado_venta=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_estado_venta),self.estado_venta)	

class TipoPago(models.Model):
	id_tipo_pago=models.AutoField(primary_key=True)
	tipo_pago=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_tipo_pago),self.tipo_pago)

class Venta(models.Model):
	id_venta=models.AutoField(primary_key=True)
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
	tipo_pago=models.ForeignKey(TipoPago, on_delete=models.CASCADE)
	fecha_venta=models.DateField()
	estado_venta=models.ForeignKey(EstadoVenta, on_delete=models.CASCADE)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4}"
		return cadena.format(str(self.id_venta),str(self.cliente.usuario),self.tipo_pago.id_tipo_pago,str(self.fecha_venta),str(self.estado_venta.id_estado_venta))

class DetalleVenta(models.Model):
	id_venta=models.ForeignKey(Venta, on_delete=models.CASCADE)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad=models.IntegerField()
	precio=models.FloatField()

	def __str__(self):
		cadena="{0}-{1},{2},{3}"
		return cadena.format(str(self.id_venta.id_venta),str(self.producto.id_producto),str(self.cantidad),str(self.precio))


class Oferta(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	porciento_desc=models.IntegerField()
	fecha_inicio=models.DateField()
	fecha_final=models.DateField()

	def __str__(self):
		cadena="{0}-{1},{2}.{3}"
		return cadena.format(str(self.producto),str(self.porciento_desc),str(self.fecha_inicio),str(self.fecha_final))



