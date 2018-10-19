# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from app.producto.models import Producto


# Create your models here.
#Procesador
class FamiliaProcesador(models.Model):
	id_familia_procesador=models.AutoField(primary_key=True)
	familia_procesador=models.CharField(max_length=25)


	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_familia_procesador),self.familia_procesador)

class ModeloProcesador(models.Model):
	id_modelo_procesador=models.AutoField(primary_key=True)	
	modelo_procesador=models.CharField(max_length=6)


	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_procesador),self.modelo_procesador)

class CacheProcesador(models.Model):
	id_cache_procesador=models.AutoField(primary_key=True)
	cache_procesador=models.CharField(max_length=2)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_cache_procesador),self.cache_procesador)

class PesoYDimension(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	profundidad_mm=models.PositiveIntegerField()
	altura_mm=models.PositiveIntegerField()
	anchura_mm=models.PositiveIntegerField()
	peso_g=models.PositiveIntegerField()


	def __str__(self):
		cadena="{0}-{1},{2},{3},{4}"
		return cadena.format(str(self.producto),str(self.profundidad_mm),str(self.altura_mm),str(self.anchura_mm),str(self.peso_g))

class TipoMemoria(models.Model): #procesador, tarjeta madre, ram
	id_tipo_memoria=models.AutoField(primary_key=True)
	tipo_memoria=models.CharField(max_length=8)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_tipo_memoria),self.tipo_memoria)

class SocketProcesador(models.Model):
	id_socket_procesdor=models.AutoField(primary_key=True)
	socket_procesador=models.CharField(max_length=10)
	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_socket_procesdor),self.socket_procesador)

class Litografia(models.Model):
	id_litografia=models.AutoField(primary_key=True)
	litografia_nm=models.CharField(max_length=5)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_litografia),self.litografia_nm)

class SO(models.Model):
	id_so=models.AutoField(primary_key=True)
	so=models.CharField(max_length=16)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_so),self.so)

#Tarjetas de vídeo


class ModeloGrafica(models.Model):
	id_modelo_grafica=models.AutoField(primary_key=True)
	modelo_grafica=models.CharField(max_length=15, blank=True, null=True)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_grafica),self.modelo_grafica)		

class ProcesadorGrafico(models.Model):
	id_procesador_grafico=models.AutoField(primary_key=True)
	procesador_grafico=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_procesador_grafico),self.procesador_grafico)

class TipoInterfaz(models.Model):
	id_tipo_interfaz=models.AutoField(primary_key=True)
	tipo_interfaz=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_tipo_interfaz),self.tipo_interfaz)

class FamiliaGrafica(models.Model):
	id_familia_grafica=models.AutoField(primary_key=True)
	familia_grafica=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_familia_grafica),self.familia_grafica)

class TipoMemoriaGrafica(models.Model):
	id_tipo_memoria_grafica=models.AutoField(primary_key=True)
	tipo_memoria_grafica=models.CharField(max_length=6)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_tipo_memoria_grafica),self.tipo_memoria_grafica)	
#Universal
class Color(models.Model):
	id_color=models.AutoField(primary_key=True)
	color=models.CharField(max_length=10)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_color),self.color)

#Disco Duro		
class ModeloDD(models.Model):
	id_modelo_dd=models.AutoField(primary_key=True)
	modelo_dd=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_dd),self.modelo_dd)

class RPM(models.Model):
	id_rpm=models.AutoField(primary_key=True)
	rpm=models.PositiveIntegerField()

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_rpm),str(self.rpm))

class TamDD(models.Model):
	id_tamdd=models.AutoField(primary_key=True)
	tamdd=models.FloatField()

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_tamdd),str(self.tamdd))

class InterfazDD(models.Model):
	id_interfazdd=models.AutoField(primary_key=True)
	interfazdd=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_interfazdd),self.interfazdd)

#RAM

class ModeloRAM(models.Model):
	id_modelo_ram=models.AutoField(primary_key=True)
	modelo_ram=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_ram),self.modelo_ram)

class FactorFormaRAM(models.Model):
	id_factor_forma_ram=models.AutoField(primary_key=True)
	factor_forma_ram=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_factor_forma_ram),self.factor_forma_ram)			
#PSU
class ModeloPSU(models.Model):
	id_modelo_psu=models.AutoField(primary_key=True)
	modelo_psu=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_psu),self.modelo_psu)

class FactorForma(models.Model):
	id_factor_forma=models.AutoField(primary_key=True)
	factor_forma=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_factor_forma),self.factor_forma)

class Certificacion(models.Model):
	id_certificacion=models.AutoField(primary_key=True)
	certificacion=models.CharField(max_length=17)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_certificacion),self.certificacion)

#Tarjeta madre
class ModeloTarjetaMadre(models.Model):
	id_modelo_tarjeta_madre=models.AutoField(primary_key=True)
	modelo_tarjeta_madre=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_tarjeta_madre),self.modelo_tarjeta_madre)

class Chipset(models.Model):
	id_chipset=models.AutoField(primary_key=True)
	chipset=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_chipset),self.chipset)


#Gabinete

class ModeloGabinete(models.Model):
	id_modelo_gabinete=models.AutoField(primary_key=True)
	modelo_gabinete=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_gabinete),self.modelo_gabinete)

class FactorFormaGabinete(models.Model):
	id_factor_forma_gabinete=models.AutoField(primary_key=True)
	factor_forma_gabinete=models.CharField(max_length=10)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_factor_forma_gabinete),self.factor_forma_gabinete)

#Teclado
class ModeloTeclado(models.Model):
	id_modelo_teclado=models.AutoField(primary_key=True)
	modelo_teclado=models.CharField(max_length=20)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_teclado),self.modelo_teclado)

class Conectividad(models.Model):
	id_conectividad=models.AutoField(primary_key=True)
	conectividad=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_conectividad),self.conectividad)				

class Idioma(models.Model):
	id_idioma=models.AutoField(primary_key=True)
	idioma=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_idioma),self.idioma)

#Mouse
class ModeloMouse(models.Model):
	id_modelo_mouse=models.AutoField(primary_key=True)
	modelo_mouse=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_mouse),self.modelo_mouse)

#Monitor

class ModeloMonitor(models.Model):
	id_modelo_monitor=models.AutoField(primary_key=True)
	modelo_monitor=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_modelo_monitor),self.modelo_monitor)

class RelacionAspecto(models.Model):
	id_relacion_aspecto=models.AutoField(primary_key=True)
	relacion_aspecto=models.CharField(max_length=5)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_relacion_aspecto),self.relacion_aspecto)

class Resolucion(models.Model):
	id_resolucion=models.AutoField(primary_key=True)
	resolucion=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_resolucion),self.resolucion)

class HD(models.Model):
	id_hd=models.AutoField(primary_key=True)
	hd=models.CharField(max_length=15)

	def __str__(self):
		cadena="{0}-{1}"
		return cadena.format(str(self.id_hd),self.hd)											