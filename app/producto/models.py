# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Marca(models.Model):
	id_marca=models.AutoField(primary_key=True)
	marca=models.CharField(max_length=30)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_marca),self.marca)

class Categoria(models.Model):
	id_categoria=models.PositiveIntegerField(primary_key=True)
	categoria=models.CharField(max_length=30)
	imagen_categoria=models.ImageField(upload_to='categorias')


	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_categoria),self.categoria)

class Producto(models.Model):
    id_producto=models.AutoField(primary_key=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE)
    stock_min=models.IntegerField()
    stock_max=models.IntegerField()
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    fecha_registro=models.DateField()
    estado_producto=models.CharField(max_length=1)

    def __str__(self):
	    cadena="{0}-{1},{2},{3},{4},{5},{6}"
	    return cadena.format(str(self.id_producto),self.categoria.categoria,self.marca.marca, str(self.stock_min),str(self.stock_max), str(self.cantidad),str(self.precio),str(self.fecha_registro),self.estado_producto)
	

class ImagenProducto(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	imagen_principal=models.ImageField(upload_to='productos')
	imagen1=models.ImageField(upload_to='productos', null=True, blank=True)
	imagen2=models.ImageField(upload_to='productos', null=True, blank=True)
	imagen3=models.ImageField(upload_to='productos', null=True, blank=True)


class Comentario(models.Model):
	id_comentario=models.AutoField(primary_key=True)
	usuario=models.ForeignKey(User,on_delete=models.CASCADE)
	producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
	comentario=models.TextField(max_length=300)
	fecha_comentario=models.DateField(blank=True, null=True)


	def __str__(self):
		cadena="{0}-{1},{2},{3}"
		return cadena.format(str(self.id_comentario),self.usuario.username,str(self.producto), self.comentario)



