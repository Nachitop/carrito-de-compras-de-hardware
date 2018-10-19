# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from app.producto.models import Producto, Marca
#Procesador
from app.caracteristicas.models import FamiliaProcesador, ModeloProcesador, SocketProcesador, CacheProcesador, Litografia, SO, TipoMemoria
#Tarjetas de video
from app.caracteristicas.models import ProcesadorGrafico, TipoInterfaz, FamiliaGrafica, TipoMemoriaGrafica, Color, ModeloGrafica
#DD y SSD
from app.caracteristicas.models import RPM, TamDD, InterfazDD, ModeloDD
#RAM
from app.caracteristicas.models import FactorFormaRAM, ModeloRAM
#PSU
from app.caracteristicas.models import FactorForma, Certificacion, ModeloPSU
#Tarjeta Madre
from app.caracteristicas.models import Chipset, ModeloTarjetaMadre
#Gabinete
from app.caracteristicas.models import ModeloGabinete, FactorFormaGabinete
#Teclado
from app.caracteristicas.models import ModeloTeclado, Conectividad, Idioma
#Mouse
from app.caracteristicas.models import ModeloMouse
#Monitor
from app.caracteristicas.models import ModeloMonitor, RelacionAspecto, Resolucion, HD
# Create your models here.

#def nombre(self):
#	cadena="{}-{}"
#	return cadena=(str(self.producto)+str(self.familia_procesador))

class Procesador(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	familia_procesador=models.ForeignKey(FamiliaProcesador, on_delete=models.CASCADE)
	modelo_procesador=models.ForeignKey(ModeloProcesador, on_delete=models.CASCADE)
	socket_procesador=models.ForeignKey(SocketProcesador, on_delete=models.CASCADE)
	frecuencia_mhz=models.FloatField()
	frecuencia_turbo_mhz=models.FloatField()
	disipador=models.BooleanField()
	cache_procesador=models.ForeignKey(CacheProcesador, on_delete=models.CASCADE)
	cantidad_cache=models.PositiveIntegerField()
	nucleos=models.PositiveIntegerField()
	hilos=models.PositiveIntegerField()
	litografia=models.ForeignKey(Litografia, on_delete=models.CASCADE)
	so=models.ForeignKey(SO, on_delete=models.CASCADE)
	cantidad_memoria_mhz=models.PositiveIntegerField(blank=True, null=True)
	tipo_memoria=models.ForeignKey(TipoMemoria, on_delete=models.CASCADE)
	adaptador_grafico=models.BooleanField()
	tdp=models.PositiveIntegerField()

	#__str__=nombre
	

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15}"
		return cadena.format(str(self.producto),self.familia_procesador.familia_procesador, self.modelo_procesador.modelo_procesador,self.socket_procesador.
			socket_procesador,str(self.frecuencia_mhz),str(self.frecuencia_turbo_mhz),str(self.disipador),self.cache_procesador.cache_procesador,str(self.cantidad_cache),
			str(self.nucleos),str(self.hilos),self.litografia.litografia_nm,self.so.so,self.tipo_memoria.tipo_memoria,str(self.adaptador_grafico),str(self.tdp))

class TarjetaVideo(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	familia_grafica=models.ForeignKey(FamiliaGrafica, on_delete=models.CASCADE)
	modelo_grafica=models.ForeignKey(ModeloGrafica, on_delete=models.CASCADE)
	procesador_grafico=models.ForeignKey(ProcesadorGrafico, on_delete=models.CASCADE)
	nucleos_cuda=models.PositiveIntegerField()
	tipo_interfaz=models.ForeignKey(TipoInterfaz, on_delete=models.CASCADE)
	frecuencia_mhz=models.PositiveIntegerField()
	frecuencia_turbo_mhz=models.PositiveIntegerField()
	memoria_grafica_gb=models.PositiveIntegerField()
	tipo_memoria_grafica=models.ForeignKey(TipoMemoriaGrafica, on_delete=models.CASCADE)
	ancho_datos_bits=models.PositiveIntegerField()
	version_directx=models.FloatField()
	cantidad_dvi=models.PositiveIntegerField()
	cantidad_hdmi=models.PositiveIntegerField()
	cantidad_displayport=models.PositiveIntegerField()
	colores=models.ManyToManyField(Color)

	#__str__=nombre

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}"
		return cadena.format(str(self.producto),self.familia_grafica.familia_grafica, self.modelo_grafica.modelo_grafica, self.procesador_grafico.procesador_grafico,str(self.nucleos_cuda),
			self.tipo_interfaz.tipo_interfaz,str(self.frecuencia_mhz),str(self.frecuencia_turbo_mhz),str(self.memoria_grafica_gb),self.tipo_memoria_grafica.tipo_memoria_grafica,
			str(self.ancho_datos_bits),str(self.version_directx),str(self.cantidad_dvi),str(self.cantidad_hdmi),str(self.cantidad_displayport), self.colores.all())

class TarjetaMadre(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_tarjeta_madre=models.ForeignKey(ModeloTarjetaMadre,on_delete=models.CASCADE)		
	familia_procesador=models.ManyToManyField(FamiliaProcesador)
	socket_procesador=models.ForeignKey(SocketProcesador, on_delete=models.CASCADE)
	chipset=models.ForeignKey(Chipset, on_delete=models.CASCADE)
	cantidad_memoria_gb=models.PositiveIntegerField()
	tipo_memoria=models.ForeignKey(TipoMemoria,on_delete=models.CASCADE)
	cantidad_ranuras_memoria=models.PositiveIntegerField()
	cantidad_puertos_pci=models.PositiveIntegerField()
	cantidad_puertos_usb3=models.PositiveIntegerField()
	cantidad_puertos_usb2=models.PositiveIntegerField()
	cantidad_puertos_sata=models.PositiveIntegerField()
	cantidad_puertos_hdmi=models.PositiveIntegerField()
	factor_forma=models.ForeignKey(FactorForma, on_delete=models.CASCADE)
	para_marca=models.ForeignKey(Marca, on_delete=models.CASCADE, blank=True, null=True)
	colores=models.ManyToManyField(Color)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}"
		return cadena.format(str(self.producto),self.modelo_tarjeta_madre.modelo_tarjeta_madre,self.socket_procesador.socket_procesador, self.chipset.chipset,
			str(self.cantidad_memoria_gb),self.tipo_memoria.tipo_memoria,str(self.cantidad_ranuras_memoria),str(self.cantidad_puertos_pci),str(self.cantidad_puertos_usb3),
			str(self.cantidad_puertos_usb2),str(self.cantidad_puertos_sata),str(self.cantidad_puertos_hdmi),self.factor_forma.factor_forma, str(self.colores.all()))


class DiscoDuro(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_dd=models.ForeignKey(ModeloDD, on_delete=models.CASCADE)
	capacidad=models.PositiveIntegerField()
	cache=models.PositiveIntegerField()
	rpm=models.ForeignKey(RPM, on_delete=models.CASCADE)
	tamdd=models.ForeignKey(TamDD,on_delete=models.CASCADE)
	interfazdd=models.ForeignKey(InterfazDD,on_delete=models.CASCADE)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6}"
		return cadena.format(str(self.producto),self.modelo_dd.modelo_dd,str(self.capacidad), str(self.cache), self.rpm.rpm, str(self.tamdd.tamdd), self.interfazdd.interfazdd)

class SSD(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_dd=models.ForeignKey(ModeloDD, on_delete=models.CASCADE)
	capacidad=models.PositiveIntegerField()
	velocidad_escritura=models.PositiveIntegerField()
	velocidad_lectura=models.PositiveIntegerField()
	tamdd=models.ForeignKey(TamDD, on_delete=models.CASCADE)
	interfazdd=models.ForeignKey(InterfazDD, on_delete=models.CASCADE)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6}"
		return cadena.format(str(self.producto),self.modelo_dd.modelo_dd,str(self.capacidad), str(self.velocidad_escritura), self.velocidad_lectura, str(self.tamdd.tamdd), self.interfazdd.interfazdd)


class RAM(models.Model):
	producto=models.OneToOneField(Producto,on_delete=models.CASCADE, primary_key=True)
	modelo_ram=models.ForeignKey(ModeloRAM, on_delete=models.CASCADE)
	cantidad_memoria_gb=models.PositiveIntegerField()
	cantidad_memoria_mhz=models.PositiveIntegerField()
	tipo_memoria=models.ForeignKey(TipoMemoria, on_delete=models.CASCADE)
	latencia=models.PositiveIntegerField()
	factor_forma_ram=models.ForeignKey(FactorFormaRAM, on_delete=models.CASCADE)
	colores=models.ManyToManyField(Color)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6},{7}"
		return cadena.format(str(self.producto),self.modelo_ram.modelo_ram,str(self.cantidad_memoria_gb), str(self.cantidad_memoria_mhz), self.tipo_memoria.tipo_memoria, str(self.latencia), self.factor_forma_ram.factor_forma_ram, (self.colores.all()))

class PSU(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_psu=models.ForeignKey(ModeloPSU, on_delete=models.CASCADE)
	potencia_nominal=models.PositiveIntegerField()
	diametro_ventilador_mm=models.PositiveIntegerField()
	factor_forma=models.ForeignKey(FactorForma,on_delete=models.CASCADE)
	conectores_sata=models.PositiveIntegerField()
	certificacion=models.ForeignKey(Certificacion, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6}"
		return cadena.format(str(self.producto),self.modelo_psu.modelo_psu, str(self.potencia_nominal), str(self.diametro_ventilador_mm),self.factor_forma.factor_forma,str(self.conectores_sata),self.certificacion.certificacion)

class Gabinete(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_gabinete=models.ForeignKey(ModeloGabinete, on_delete=models.CASCADE)
	factor_forma_gabinete=models.ForeignKey(FactorFormaGabinete, on_delete=models.CASCADE)
	mobos_soportadas=models.ManyToManyField(FactorForma)
	dd_soportados=models.ManyToManyField(TamDD)
	psu_incluida=models.BooleanField()
	potencia_nominal=models.PositiveIntegerField(blank=True, null=True)
	cantidad_puertos_usb2=models.PositiveIntegerField()
	cantidad_puertos_usb3=models.PositiveIntegerField()
	cantidad_ranuras_expansion=models.PositiveIntegerField()
	cantidad_ventiladores=models.PositiveIntegerField()
	ventana_lateral=models.BooleanField()
	colores=models.ManyToManyField(Color)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}"
		return cadena.format(str(self.producto), self.modelo_gabinete.modelo_gabinete, self.factor_forma_gabinete.factor_forma_gabinete,
			self.mobos_soportadas.all(), self.dd_soportados.all(), str(self.psu_incluida), str(self.potencia_nominal), str(self.cantidad_puertos_usb2),
			str(self.cantidad_puertos_usb3),str(self.cantidad_ranuras_expansion), str(self.cantidad_ventiladores), str(self.ventana_lateral), str(self.colores.all()))

class Teclado(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_teclado=models.ForeignKey(ModeloTeclado, on_delete=models.CASCADE)
	tipo_interfaz=models.ForeignKey(TipoInterfaz, on_delete=models.CASCADE)
	conectividad=models.ForeignKey(Conectividad, on_delete=models.CASCADE)
	idioma=models.ForeignKey(Idioma, on_delete=models.CASCADE)
	rgb=models.BooleanField()
	colores=models.ManyToManyField(Color)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6}"
		return cadena.format(str(self.producto), self.modelo_teclado.modelo_teclado, self.tipo_interfaz.tipo_interfaz, self.conectividad.conectividad, self.idioma.idioma, str(self.rgb),str(self.colores.all()))		

class Mouse(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_mouse=models.ForeignKey(ModeloMouse, on_delete=models.CASCADE)
	tipo_interfaz=models.ForeignKey(TipoInterfaz, on_delete=models.CASCADE)
	conectividad=models.ForeignKey(Conectividad, on_delete=models.CASCADE)
	dpi=models.PositiveIntegerField()
	rgb=models.BooleanField()
	colores=models.ManyToManyField(Color)

	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6}"
		return cadena.format(str(self.producto), self.modelo_mouse.modelo_mouse, self.tipo_interfaz.tipo_interfaz, self.conectividad.conectividad, str(self.dpi), str(self.rgb),str(self.colores.all()))

class Monitor(models.Model):
	producto=models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
	modelo_monitor=models.ForeignKey(ModeloMonitor, on_delete=models.CASCADE)
	tam_pantalla=models.FloatField()
	relacion_aspecto=models.ForeignKey(RelacionAspecto, on_delete=models.CASCADE)
	resolucion=models.ForeignKey(Resolucion, on_delete=models.CASCADE)
	hd=models.ForeignKey(HD, on_delete=models.CASCADE)
	cantidad_hdmi=models.PositiveIntegerField()
	cantidad_dvi=models.PositiveIntegerField()
	cantidad_vga=models.PositiveIntegerField()
	cantidad_dp=models.PositiveIntegerField()
	colores=models.ManyToManyField(Color)


	def __str__(self):
		cadena="{0}-{1},{2},{3},{4},{5},{6},{7},{8},{9}"
		return cadena.format(str(self.producto), self.modelo_monitor.modelo_monitor,str(self.tam_pantalla), self.relacion_aspecto.relacion_aspecto, self.resolucion.resolucion,
			self.hd.hd, str(self.cantidad_hdmi), str(self.cantidad_dvi),str(self.cantidad_vga),str(self.colores.all()))






