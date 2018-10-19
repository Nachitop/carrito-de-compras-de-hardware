# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import ListView, View
from app.subproducto.models import *
from app.producto.models import *
from app.venta.models import *
from app.cliente.models import Cliente, Favorito
from app.caracteristicas.models import *
from datetime import date, timedelta
from django.forms.models import model_to_dict
import jsonpickle
from django.core import serializers
from django.db.models import Q
from itertools import chain
from django.db.models import Sum, F
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas



# Create your views here.
global hoy, dias
hoy = date.today()
dias=timedelta(days=7)

productos=Producto.objects.filter(estado_producto="A", cantidad__gte=1)
ofertas=Oferta.objects.filter(fecha_final__gte=hoy)
class ListaTotalHistorial():
	id_venta=""
	total=""
	envio=""
	cantidad=""
	id_producto=""

def historial_compras(request):
	categorias=Categoria.objects.all().order_by("categoria")
	cliente=Cliente.objects.get(usuario=request.user.id)
	estado_venta=EstadoVenta.objects.get(id_estado_venta=1)
	historial=Venta.objects.filter(cliente=cliente, estado_venta=estado_venta)
	historial_detalle=DetalleVenta.objects.filter(id_venta__in=historial)
	# print(historial_detalle)
	# productos_detalle=[]
	# for venta in historial_detalle:
	# 	print("entrééeéé")
	# 	obj_ListaTotalHistorial=ListaTotalHistorial()
	# 	obj_ListaTotalHistorial.id_venta=venta.id_venta.id_venta
	# 	obj_ListaTotalHistorial.total=str(venta.cantidad*venta.precio)
	# 	obj_ListaTotalHistorial.envio="150"
	# 	obj_ListaTotalHistorial.cantidad=venta.cantidad
	# 	obj_ListaTotalHistorial.id_producto=venta.producto.id_producto
		
	# 	productos_detalle.append(obj_ListaTotalHistorial)
	# productos_detalle2=[]
	# for d in productos_detalle:
	# 	print("entrééeéé22222222")
	# 	if not productos_detalle2:
	# 		print("aqui")
	# 		productos_detalle2.append(d)
	# 	else:
	# 		x=0
	# 		for pd in productos_detalle2:
	# 			if pd.id_venta==d.id_venta:
	# 				if pd.id_producto!=d.id_producto:
	# 					n_obj_total=ListaTotalHistorial()
	# 					n_obj_total.id_venta=d.id_venta
	# 					n_obj_total.total=str(int(d.total)+int(pd.total))
	# 					n_obj_total.envio="150"
	# 					n_obj_total.cantidad=str(int(d.cantidad)+int(pd.cantidad))
	# 					n_obj_total.id_producto="0"
	# 					productos_detalle2.pop(x)
	# 					productos_detalle2.append(n_obj_total)
	# 					x=x+1
	# 				else:
	# 					print("chill")
	# 			else:
	# 				productos_detalle2.append(pd)
	# for i in productos_detalle2:
	# 	print(i.id_venta)
	# for i in productos_detalle:
	# 	print(i.id_venta)



	contexto= {'categorias': categorias}
	contexto['historial_venta']=historial.order_by('-id_venta')
	contexto['historial_detalle']=historial_detalle
	
	return render(request,'tienda/historial.html',contexto)

def favoritos(request):
	categorias=Categoria.objects.all().order_by("categoria")
	contexto= {'categorias': categorias}
	return render(request,'tienda/favoritos.html',contexto)

class Index(ListView):
	queryset = Categoria.objects.all().order_by("categoria")
	template_name = 'tienda/index.html'
	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context['categorias'] = self.queryset
		return context

def carrito(request):
	categorias=Categoria.objects.all().order_by("categoria")
	contexto= {'categorias': categorias}
	return render(request, 'tienda/carrito.html',contexto)
		
def categorias(request):
	categorias=Categoria.objects.all().order_by("categoria")
	contexto= {'categorias': categorias}
	return render(request, 'tienda/categorias.html',contexto)

def ir_categoria(request,categoria):
	categorias=Categoria.objects.all().order_by("categoria")
	marcas=Marca.objects.all().order_by('marca')
	contexto={}
	contexto['categorias']=categorias
	if categoria=="1":
		productos_procesadores=Producto.objects.filter(categoria=1, estado_producto="A", cantidad__gte=1)
		id_procesadores=productos_procesadores.values_list('id_producto',flat=True)
		procesadores=Procesador.objects.filter(producto__in=id_procesadores)
		#familia
		id_familia_procesadores=procesadores.values_list('familia_procesador',flat=True)
		familia_procesador=FamiliaProcesador.objects.all()
		valores_familia_procesador=familia_procesador.filter(id_familia_procesador__in=id_familia_procesadores)

		#Marcas
		marca_procesadores=productos_procesadores.values_list('marca', flat=True)
		valores_marcas_procesadores=marcas.filter(id_marca__in=marca_procesadores)

		#socket
		id_socket_procesadores=procesadores.values_list('socket_procesador',flat=True)
		socket_procesador=SocketProcesador.objects.all()
		valores_socket_procesador=socket_procesador.filter(id_socket_procesdor__in=id_socket_procesadores)
		
		#cores
		num_cores=procesadores.values_list('nucleos',flat=True).distinct()


		#contextos
		contexto['marcas']=valores_marcas_procesadores
		contexto['familias']=valores_familia_procesador
		contexto['sockets']=valores_socket_procesador
		contexto['cores']=num_cores

		return render(request,'tienda/procesadores.html',contexto)
	elif categoria=="2":
		productos_graficas=Producto.objects.filter(categoria=2,estado_producto="A",cantidad__gte=1)
		id_graficas=productos_graficas.values_list('id_producto',flat=True)
		graficas=TarjetaVideo.objects.filter(producto__in=id_graficas)
		#marcas
		marcas_graficas=productos_graficas.values_list('marca',flat=True)
		valores_marcas_graficas=marcas.filter(id_marca__in=marcas_graficas)
		#familia 
		id_familia_graficas=graficas.values_list('familia_grafica',flat=True)
		familia_grafica=FamiliaGrafica.objects.all()
		valores_familia_grafica=familia_grafica.filter(id_familia_grafica__in=id_familia_graficas)

		#procesador grafico
		id_procesadores_graficos=graficas.values_list('procesador_grafico',flat=True)
		procesador_grafico=ProcesadorGrafico.objects.all()
		valores_procesador_grafico=procesador_grafico.filter(id_procesador_grafico__in=id_procesadores_graficos)

		#memorias
		memorias=graficas.values_list('memoria_grafica_gb',flat=True).distinct()
		#tipo de memoria
		id_tipos_memorias=graficas.values_list('tipo_memoria_grafica',flat=True)
		tipo_memoria=TipoMemoriaGrafica.objects.all()
		valores_tipo_memorias_graficas=tipo_memoria.filter(id_tipo_memoria_grafica__in=id_tipos_memorias)


		contexto['marcas']=valores_marcas_graficas
		contexto['familias']=valores_familia_grafica
		contexto['procesadoresgraficos']=valores_procesador_grafico
		contexto['memorias']=memorias
		contexto['tipos_memorias']=valores_tipo_memorias_graficas
		return render(request,'tienda/graficas.html',contexto)
	elif categoria=="3":
		productos_mobos=Producto.objects.filter(categoria=3,estado_producto="A",cantidad__gte=1)
		id_mobos=productos_mobos.values_list('id_producto',flat=True)
		mobos=TarjetaMadre.objects.filter(producto__in=id_mobos)

		#marcas
		marcas_mobos=productos_mobos.values_list('marca',flat=True)
		valores_marcas_mobos=marcas.filter(id_marca__in=marcas_mobos)

		#Familia
		id_familia_mobos=mobos.values_list('familia_procesador',flat=True)
		familia_mobos=FamiliaProcesador.objects.all()
		valores_familia_mobos=familia_mobos.filter(id_familia_procesador__in=familia_mobos)

		#socket
		id_sockets=mobos.values_list('socket_procesador',flat=True)
		sockets=SocketProcesador.objects.all()
		valores_socket_procesador=sockets.filter(id_socket_procesdor__in=id_sockets)

		#chipset
		id_chipsets=mobos.values_list('chipset',flat=True)
		chipsets=Chipset.objects.all()
		valores_chipset_mobos=chipsets.filter(id_chipset__in=id_chipsets)

		#memoria
		cantidad_memoria=mobos.values_list('cantidad_memoria_gb',flat=True).distinct()
		#tipo de memoria
		id_tipo_memorias=mobos.values_list('tipo_memoria',flat=True)
		tipo_memoria=TipoMemoria.objects.all()
		valores_tipos_memoria=tipo_memoria.filter(id_tipo_memoria__in=id_tipo_memorias)

		#factor forma
		id_factor_formas=mobos.values_list('factor_forma',flat=True)
		factor_forma=FactorForma.objects.all()
		valores_factor_forma=factor_forma.filter(id_factor_forma__in=id_factor_formas)

		#Para
		id_paras=mobos.values_list('para_marca',flat=True)
		paras=Marca.objects.all()
		valores_paras=paras.filter(id_marca__in=id_paras)


		#contexto
		contexto['marcas']=valores_marcas_mobos
		contexto['familias']=valores_familia_mobos
		contexto['sockets']=valores_socket_procesador
		contexto['chipsets']=valores_chipset_mobos
		contexto['memorias']=cantidad_memoria
		contexto['tipos']=valores_tipos_memoria
		contexto['formas']=valores_factor_forma
		contexto['paras']=valores_paras
		return render(request,'tienda/mobos.html',contexto)
	elif categoria=="4":
		productos_ssd=Producto.objects.filter(categoria=4,estado_producto="A",cantidad__gte=1)
		id_ssds=productos_ssd.values_list('id_producto',flat=True)
		ssds=SSD.objects.filter(producto__in=id_ssds)

		#marca
		marcas_ssds=productos_ssd.values_list('marca',flat=True)
		valores_marcas_ssds=marcas.filter(id_marca__in=marcas_ssds)

		#capacidades
		valores_capacidades=ssds.values_list('capacidad',flat=True).distinct()
		#interfaces
		id_interfaces=ssds.values_list('interfazdd',flat=True)
		interfaz=InterfazDD.objects.all()
		valores_interfaces=interfaz.filter(id_interfazdd__in=id_interfaces)

		#contextos
		contexto['marcas']=valores_marcas_ssds
		contexto['capacidades']=valores_capacidades
		contexto['interfaces']=valores_interfaces
		return render(request,'tienda/ssds.html',contexto) 
	elif categoria=="5":
		productos_dds=Producto.objects.filter(categoria=5,estado_producto="A",cantidad__gte=1)
		id_dds=productos_dds.values_list('id_producto',flat=True)
		dds=DiscoDuro.objects.filter(producto__in=id_dds)
		#marcas
		id_marcas_dds=productos_dds.values_list('marca',flat=True)
		valores_marcas_dd=marcas.filter(id_marca__in=id_marcas_dds)
		#capacidades
		valores_capacidades=dds.values_list('capacidad',flat=True).distinct()
		#interfaces
		id_interfaces=dds.values_list('interfazdd',flat=True)
		interfaz=InterfazDD.objects.all()
		valores_interfaces=interfaz.filter(id_interfazdd__in=id_interfaces)
		#cache
		valores_caches=dds.values_list('cache',flat=True).distinct()
		#RPM
		id_rpms=dds.values_list('rpm',flat=True).distinct()
		rpm=RPM.objects.all()
		valores_rpms=rpm.filter(id_rpm__in=id_rpms)
		#tamanos
		id_tamdds=dds.values_list('tamdd',flat=True).distinct()
		tamdd=TamDD.objects.all()
		valores_tamdds=tamdd.filter(id_tamdd__in=id_tamdds)

		#contextos
		contexto['marcas']=valores_marcas_dd
		contexto['capacidades']=valores_capacidades
		contexto['interfaces']=valores_interfaces
		contexto['caches']=valores_caches
		contexto['rpms']=valores_rpms
		contexto['tamdds']=valores_tamdds
		return render(request,'tienda/dds.html',contexto) 
	elif categoria=="6":
		productos_ram=Producto.objects.filter(categoria=6,estado_producto="A",cantidad__gte=1)
		id_rams=productos_ram.values_list('id_producto',flat=True)
		rams=RAM.objects.filter(producto__in=id_rams)
		#marcas
		id_marcas_rams=productos_ram.values_list('marca',flat=True)
		valores_marcas_rams=marcas.filter(id_marca__in=id_marcas_rams)
		#cantidad GB
		valores_cantidad_gb=rams.values_list('cantidad_memoria_gb',flat=True).distinct()

		#cantidad mhz
		valores_cantidad_mhz=rams.values_list('cantidad_memoria_mhz',flat=True).distinct()

		#tipo
		id_tipos_memorias=rams.values_list('tipo_memoria',flat=True)
		tipo_memoria=TipoMemoria.objects.all()
		valores_tipos_memorias=tipo_memoria.filter(id_tipo_memoria__in=id_tipos_memorias)

		#formas
		id_formas_rams=rams.values_list('factor_forma_ram',flat=True)
		factor_forma_ram=FactorFormaRAM.objects.all()
		valores_formas=factor_forma_ram.filter(id_factor_forma_ram__in=id_formas_rams)

		#contextos
		contexto['marcas']=valores_marcas_rams
		contexto['gbs']=valores_cantidad_gb
		contexto['mhzs']=valores_cantidad_mhz
		contexto['tipos']=valores_tipos_memorias
		contexto['formas']=valores_formas

		return render(request,'tienda/rams.html',contexto)
	elif categoria=="7":
		productos_psu=Producto.objects.filter(categoria=7,estado_producto="A",cantidad__gte=1)
		id_psus=productos_psu.values_list('id_producto',flat=True)
		psus=PSU.objects.filter(producto__in=id_psus)
		#marcas
		id_marcas_psus=productos_psu.values_list('marca',flat=True)
		valores_marcas_psus=marcas.filter(id_marca__in=id_marcas_psus)

		valores_potencias=psus.values_list('potencia_nominal',flat=True).distinct()
		#factor de forma
		id_factor_formas=psus.values_list('factor_forma',flat=True)
		factor_forma=FactorForma.objects.all()
		valores_factores=factor_forma.filter(id_factor_forma__in=id_factor_formas)
		#certificaciones
		id_certificaciones=psus.values_list('certificacion',flat=True)
		certificacion=Certificacion.objects.all()
		valores_certificaciones=certificacion.filter(id_certificacion__in=id_certificaciones)

		#contextos
		contexto['marcas']=valores_marcas_psus
		contexto['potencias']=valores_potencias
		contexto['formas']=valores_factores
		contexto['certificaciones']=valores_certificaciones

		return render(request,'tienda/psus.html',contexto) 
	elif categoria=="8":
		productos_gabinete=Producto.objects.filter(categoria=8,estado_producto="A",cantidad__gte=1)
		id_gabos=productos_gabinete.values_list('id_producto',flat=True)
		gabos=Gabinete.objects.filter(producto__in=id_gabos)
		#marcas
		id_marcas_gabos=productos_gabinete.values_list('marca',flat=True)
		valores_marcas_gabos=marcas.filter(id_marca__in=id_marcas_gabos)
		#factor de forma
		id_factor_formas=gabos.values_list('factor_forma_gabinete',flat=True)
		factor_forma=FactorFormaGabinete.objects.all()
		valores_factores=factor_forma.filter(id_factor_forma_gabinete__in=id_factor_formas)
		#contextos
		contexto['marcas']=valores_marcas_gabos
		contexto['formas']=valores_factores
		return render(request,'tienda/gabos.html',contexto)

	elif categoria=="9":
		productos_teclados=Producto.objects.filter(categoria=9,estado_producto="A",cantidad__gte=1)
		id_teclados=productos_teclados.values_list('id_producto',flat=True)
		teclados=Teclado.objects.filter(producto__in=id_teclados)
		#marcas
		id_marcas_teclados=productos_teclados.values_list('marca',flat=True)
		valores_marcas_teclados=marcas.filter(id_marca__in=id_marcas_teclados)

		#conectividades
		
		id_conectividades=teclados.values_list('conectividad',flat=True)
		
		conectividad=Conectividad.objects.all()
		valores_conectividades=conectividad.filter(id_conectividad__in=id_conectividades)
		
		#contextos
		contexto['marcas']=valores_marcas_teclados
		contexto['conectividades']=valores_conectividades
		return render(request,'tienda/teclados.html',contexto)
	elif categoria=="10":
		productos_mouses=Producto.objects.filter(categoria=10,estado_producto="A",cantidad__gte=1)
		id_mouses=productos_mouses.values_list('id_producto',flat=True)
		mouses=Mouse.objects.filter(producto__in=id_mouses)
		#marcas
		id_marcas_mouses=productos_mouses.values_list('marca',flat=True)
		valores_marcas_mouse=marcas.filter(id_marca__in=id_marcas_mouses)
		#conectividades
		id_conectividades=mouses.values_list('conectividad',flat=True)
		
		conectividad=Conectividad.objects.all()
		valores_conectividades=conectividad.filter(id_conectividad__in=id_conectividades)
		#contextos
		contexto['marcas']=valores_marcas_mouse
		contexto['conectividades']=valores_conectividades
		return render(request,'tienda/mouses.html',contexto)
	elif categoria=="11":
		productos_monitores=Producto.objects.filter(categoria=11,estado_producto="A",cantidad__gte=1)
		id_monitores=productos_monitores.values_list('id_producto',flat=True)
		monitores=Monitor.objects.filter(producto__in=id_monitores)
		#marcas
		id_marcas_monitores=productos_monitores.values_list('marca',flat=True)
		valores_marcas_monitor=marcas.filter(id_marca__in=id_marcas_monitores)
		#pantallas
		valores_pantallas=monitores.values_list('tam_pantalla',flat=True).distinct()
		#resoluciones
		id_resoluciones=monitores.values_list('resolucion',flat=True)
		resolucion=Resolucion.objects.all()
		valores_resoluciones=resolucion.filter(id_resolucion__in=id_resoluciones)
		#contexto
		contexto['marcas']=valores_marcas_monitor
		contexto['pantallas']=valores_pantallas
		contexto['resoluciones']=valores_resoluciones
		return render(request,'tienda/monitores.html',contexto)    

	else:
		return render(request,'tienda/index.html',contexto)  




class Product():
	#Todos tienen
	id_producto=""
	id_categoria=""
	id_marca=""
	categoria=""
	marca=""
	modelo=""
	precio=""
	precio_oferta=""
	imagen=""
	colores=""

	#Procesador
	familia_procesador=""
	frecuencia_mhz=""
	socket_procesador=""
	nucleos=""
	cantidad_cache=""
	cache_procesador=""
	tipo_cache=""

	#Tarjeta de video
	familia_grafica=""
	modelo_grafica=""
	procesador_grafico=""
	tipo_interfaz=""
	memoria_grafica_gb=""
	tipo_memoria_grafica=""
	ancho_datos_bits=""
	version_directx=""

	#Tarjeta madre
	chipset=""
	tipo_memoria=""
	factor_forma=""
	para_marca=""
	#DD
	capacidad=""
	rpm=""
	tamdd=""
	interfazdd=""
	#RAM
	cantidad_memoria_mhz=""
	cantidad_memoria_gb=""
	#PSU
	potencia_nominal=""
	certificacion=""
	#Gabinete
	factor_forma_gabinete=""
	mobos_soportadas=""
	psu_incluida=""
	ventana=""

	#Teclado
	tipo_interfaz=""
	conectividad=""
	idioma=""
	#Mouse
	dpi=""
	#monitor
	tam_pantalla=""
	relacion_aspecto=""
	resolucion=""
	hd=""




#Producto Recien llegado
def ofertas_listado(request):
	categorias=Categoria.objects.all().order_by("categoria")
	contexto= {'categorias': categorias}
	id_productos_ofertas=ofertas.values_list('producto',flat=True)
	productos_ofertas=productos.filter(id_producto__in=id_productos_ofertas)
	id_categorias_productos_ofertas=productos_ofertas.values_list('categoria',flat=True)
	categorias2=Categoria.objects.filter(id_categoria__in=id_categorias_productos_ofertas)

	contexto['categorias2']=categorias2
	return render(request, 'tienda/ofertas.html', contexto)

def recien_llegado(request):
	categorias=Categoria.objects.all().order_by("categoria")
	productos_nuevos=productos.filter(fecha_registro__gte=(hoy-dias))
	
	
	id_categorias_productos_nuevos=productos_nuevos.values_list('categoria',flat=True)
	categorias2=Categoria.objects.filter(id_categoria__in=id_categorias_productos_nuevos)
	contexto= {'categorias': categorias}
	contexto['categorias2']=categorias2
	return render(request, 'tienda/recien_llegado.html', contexto)


def obtener_productos2(productos):
	lista_productos=[]
	for producto in productos:
		obj_producto=Product()
		obj_producto.id_producto=str(producto.id_producto)
		obj_producto.id_categoria=str(producto.categoria.id_categoria)
		obj_producto.id_marca=str(producto.marca.id_marca)
		obj_producto.categoria=producto.categoria.categoria
		obj_producto.marca=producto.marca.marca
		obj_producto.precio=str(producto.precio)
		imagenes=ImagenProducto.objects.get(producto=producto.id_producto)
		obj_producto.imagen=str(imagenes.imagen_principal)  
		
		if ofertas.filter(producto=producto.id_producto).exists():
			
			
			obtener_oferta=ofertas.get(producto=producto.id_producto)
			obj_producto.precio_oferta=producto.precio-(obtener_oferta.porciento_desc*producto.precio)/100
			
		  
		

		if Procesador.objects.filter(producto=producto.id_producto).exists():
			procesador= Procesador.objects.get(producto=producto.id_producto)
			obj_producto.modelo=procesador.modelo_procesador.modelo_procesador
			obj_producto.familia_procesador=procesador.familia_procesador.familia_procesador
			obj_producto.socket_procesador="S-"+procesador.socket_procesador.socket_procesador
			obj_producto.nucleos=str(procesador.nucleos)
			obj_producto.cantidad_cache=str(procesador.cantidad_cache)
			obj_producto.cache_procesador=procesador.cache_procesador.cache_procesador

		elif TarjetaVideo.objects.filter(producto=producto.id_producto).exists():
			tarjetavideo=TarjetaVideo.objects.get(producto=producto.id_producto)
			obj_producto.modelo=tarjetavideo.modelo_grafica.modelo_grafica
			obj_producto.familia_grafica=tarjetavideo.familia_grafica.familia_grafica
			obj_producto.procesador_grafico=tarjetavideo.procesador_grafico.procesador_grafico
			obj_producto.tipo_interfaz=tarjetavideo.tipo_interfaz.tipo_interfaz
			obj_producto.memoria_grafica_gb=str(tarjetavideo.memoria_grafica_gb)
			obj_producto.tipo_memoria_grafica=tarjetavideo.tipo_memoria_grafica.tipo_memoria_grafica
			obj_producto.ancho_datos_bits=str(tarjetavideo.ancho_datos_bits)
			obj_producto.version_directx=tarjetavideo.version_directx
			obj_producto.modelo_grafica=tarjetavideo.modelo_grafica.modelo_grafica

		elif TarjetaMadre.objects.filter(producto=producto.id_producto).exists():
			tarjetamadre=TarjetaMadre.objects.get(producto=producto.id_producto)
			obj_producto.modelo=tarjetamadre.modelo_tarjeta_madre.modelo_tarjeta_madre
			obj_producto.socket_procesador=tarjetamadre.socket_procesador.socket_procesador
			obj_producto.chipset=tarjetamadre.chipset.chipset
			obj_producto.cantidad_memoria_gb=str(tarjetamadre.cantidad_memoria_gb)
			obj_producto.tipo_memoria=tarjetamadre.tipo_memoria.tipo_memoria
			obj_producto.factor_forma=tarjetamadre.factor_forma.factor_forma
			obj_producto.para_marca=tarjetamadre.para_marca.marca

		elif DiscoDuro.objects.filter(producto=producto.id_producto).exists():
			dd=DiscoDuro.objects.get(producto=producto.id_producto)
			obj_producto.modelo=dd.modelo_dd.modelo_dd
			obj_producto.capacidad=str(dd.capacidad)
			obj_producto.cache=str(dd.cache)
			obj_producto.rpm= str(dd.rpm.rpm)
			obj_producto.tamdd= str(dd.tamdd.tamdd)
			obj_producto.tipo_interfaz=dd.interfazdd.interfazdd

		elif SSD.objects.filter(producto=producto.id_producto).exists():
			ssd=SSD.objects.get(producto=producto.id_producto)
			obj_producto.modelo=ssd.modelo_dd.modelo_dd
			obj_producto.capacidad=str(ssd.capacidad)
			obj_producto.tamdd= str(ssd.tamdd.tamdd)
			obj_producto.tipo_interfaz=ssd.interfazdd.interfazdd

		elif RAM.objects.filter(producto=producto.id_producto).exists():
			ram=RAM.objects.get(producto=producto.id_producto)
			obj_producto.modelo=ram.modelo_ram.modelo_ram
			obj_producto.cantidad_memoria_gb=str(ram.cantidad_memoria_gb)
			obj_producto.cantidad_memoria_mhz=str(ram.cantidad_memoria_mhz)
			obj_producto.tipo_memoria= ram.tipo_memoria.tipo_memoria

		elif PSU.objects.filter(producto=producto.id_producto).exists():
			psu=PSU.objects.get(producto=producto.id_producto)
			obj_producto.modelo=psu.modelo_psu.modelo_psu
			obj_producto.potencia_nominal=str(psu.potencia_nominal)
			obj_producto.certificacion=psu.certificacion.certificacion
			obj_producto.factor_forma=psu.factor_forma.factor_forma

		elif Gabinete.objects.filter(producto=producto.id_producto).exists():
			gabinete=Gabinete.objects.get(producto=producto.id_producto)
			obj_producto.modelo=gabinete.modelo_gabinete.modelo_gabinete
			obj_producto.factor_forma_gabinete=gabinete.factor_forma_gabinete.factor_forma_gabinete
			if gabinete.ventana_lateral==True:
				obj_producto.ventana="Ventana lateral"
			if gabinete.psu_incluida==True:
				obj_producto.psu_incluida="C/Fuente de poder"+ str(gabinete.potencia_nominal)
			else:
				obj_producto.psu_incluida="S/Fuente de poder"
				   

		elif Teclado.objects.filter(producto=producto.id_producto).exists():        
			teclado=Teclado.objects.get(producto=producto.id_producto)
			obj_producto.modelo=teclado.modelo_teclado.modelo_teclado
			obj_producto.tipo_interfaz=teclado.tipo_interfaz.tipo_interfaz
			obj_producto.conectividad=teclado.conectividad.conectividad
			obj_producto.idioma =teclado.idioma.idioma

		elif Mouse.objects.filter(producto=producto.id_producto).exists():          
			mouse=Mouse.objects.get(producto=producto.id_producto)
			obj_producto.modelo=mouse.modelo_mouse.modelo_mouse
			obj_producto.tipo_interfaz=mouse.tipo_interfaz.tipo_interfaz
			obj_producto.conectividad=mouse.conectividad.conectividad
			obj_producto.dpi =str(mouse.dpi)

		elif Monitor.objects.filter(producto=producto.id_producto).exists():        
			monitor=Monitor.objects.get(producto=producto.id_producto)
			obj_producto.modelo=monitor.modelo_monitor.modelo_monitor
			obj_producto.tam_pantalla =str(monitor.tam_pantalla)
			obj_producto.relacion_aspecto=monitor.relacion_aspecto.relacion_aspecto
			obj_producto.resolucion=monitor.resolucion.resolucion
			obj_producto.hd=monitor.hd.hd

		ObjProducto=jsonpickle.encode(obj_producto)
		
		   
		lista_productos.append(ObjProducto)
		 
	return lista_productos



def obtener_ofertas_inicio(request):    
	ofertas_inicio=ofertas.values_list('producto',flat=True)
	producto_ofertas_inicio=productos.filter(id_producto__in=ofertas_inicio).order_by('precio')
	lista_productos2=obtener_productos2(producto_ofertas_inicio)
	lista_productos=[]
	x=0
	for producto in lista_productos2:
		x=x+1
		if x<=8:
			lista_productos.append(producto)

	data={}
	data["productos"]=list(lista_productos)
	return JsonResponse(data, safe=False)

def obtener_productos_nuevos_inicio(request):    
	producto_nuevos_inicio=productos.filter(fecha_registro__gte=(hoy-dias)).order_by('precio')
	lista_productos2=obtener_productos2(producto_nuevos_inicio)
	lista_productos=[]
	x=0
	for producto in lista_productos2:
		x=x+1
		if x<=8:
			lista_productos.append(producto)

	data={}
	data["productos"]=list(lista_productos)
	return JsonResponse(data, safe=False)

def obtener_productos_nuevos(request):
	
	producto_nuevos_inicio=productos.filter(fecha_registro__gte=(hoy-dias)).order_by('precio')
	lista_productos=obtener_productos2(producto_nuevos_inicio)
	cantidad_productos=len(lista_productos)
	
	data={}
	data["productos"]=list(lista_productos)
	data["cantidad"]=cantidad_productos
	return JsonResponse(data, safe=False)

def obtener_marcas(request):
	id_categoria=request.GET.get('id_categoria',None)
	productos_categoria=productos.filter(categoria=id_categoria, fecha_registro__gte=(hoy-dias)).order_by('precio')
	lista_productos=obtener_productos2(productos_categoria)
	marcas=productos_categoria.values_list('marca', flat=True).distinct()
	lista_marcas=Marca.objects.filter(id_marca__in=marcas).values()
	cantidad_productos=len(lista_productos)
	data={}
	data["productos"]=list(lista_productos)
	data["cantidad"]=cantidad_productos
	data["marcas"]=list(lista_marcas)
	return JsonResponse(data, safe=False)

def obtener_marcas_productos(request):
	id_categoria=request.GET.get('id_categoria',None)
	id_marca=request.GET.get('id_marca',None)
	productos_marcas=productos.filter(categoria=id_categoria,marca=id_marca,fecha_registro__gte=(hoy-dias))
	lista_productos=obtener_productos2(productos_marcas)
	cantidad_productos=len(lista_productos)
	data={}
	data["productos"]=list(lista_productos)
	data["cantidad"]=cantidad_productos
	return JsonResponse(data, safe=False)

	#Ofertas

def obtener_ofertas(request):
	ofertas_pag=ofertas.values_list('producto',flat=True)
	producto_ofertas=productos.filter(id_producto__in=ofertas_pag).order_by('precio')
	lista_productos=obtener_productos2(producto_ofertas)
	cantidad_productos=len(lista_productos)
	data={}
	data["productos"]=list(lista_productos)
	data["cantidad"]=cantidad_productos
	return JsonResponse(data, safe=False)


def obtener_marcas_ofertas(request):
	id_categoria=request.GET.get('id_categoria',None)
	ofertas_categorias=ofertas.values_list('producto',flat=True)
	productos_categorias=productos.filter(categoria=id_categoria,id_producto__in=ofertas_categorias)
	marcas_ofertas=productos_categorias.values_list('marca',flat=True).distinct()
	marcas=Marca.objects.filter(id_marca__in=marcas_ofertas).values()
	lista_productos=obtener_productos2(productos_categorias)
	cantidad_productos=len(lista_productos)
	data={}
	data['productos']=list(lista_productos)
	data['cantidad']=cantidad_productos
	data['marcas']=list(marcas)
	return JsonResponse(data,safe=False)

def obtener_productos_marcas_ofertas(request):
	id_categoria=request.GET.get('id_categoria',None)
	id_marca=request.GET.get('id_marca', None)
	ofertas_pag_marcas=ofertas.values_list('producto',flat=True)
	productos_marcas_ofertas=productos.filter(categoria=id_categoria,marca=id_marca, id_producto__in=ofertas_pag_marcas)
	lista_productos=obtener_productos2(productos_marcas_ofertas)
	cantidad_productos=len(lista_productos)
	data={}
	data['productos']=list(lista_productos)
	data['cantidad']=cantidad_productos
	return JsonResponse(data,safe=False)
	   
def obtener_producto(request, id_pro):
	categorias=Categoria.objects.all().order_by("categoria")
	producto=productos.get(id_producto=id_pro)
	contexto={}
	contexto['producto']=producto
	contexto['dimensiones']=PesoYDimension.objects.filter(producto=id_pro)
	print(contexto['dimensiones'])
	categoria=producto.categoria.id_categoria
	if categoria==1:
		
		contexto['procesador']=Procesador.objects.get(producto=producto.id_producto)
	elif categoria==2:
		contexto['tarjetavideo']=TarjetaVideo.objects.get(producto=producto.id_producto)
	elif categoria==3:
		contexto['tarjetamadre']=TarjetaMadre.objects.get(producto=producto.id_producto) 
	elif categoria==4:
		contexto['ssd']=SSD.objects.get(producto=producto.id_producto) 
	elif categoria==5:
		contexto['dd']=DiscoDuro.objects.get(producto=producto.id_producto) 
	elif categoria==6:
		contexto['ram']=RAM.objects.get(producto=producto.id_producto) 
	elif categoria==7:
		contexto['psu']=PSU.objects.get(producto=producto.id_producto) 
	elif categoria==8:
		contexto['gabinete']=Gabinete.objects.get(producto=producto.id_producto) 
	elif categoria==9:
		contexto['teclado']=Teclado.objects.get(producto=producto.id_producto) 
	elif categoria==10:
		contexto['mouse']=Mouse.objects.get(producto=producto.id_producto)
	elif categoria==11:
		contexto['monitor']=Monitor.objects.get(producto=producto.id_producto)      

	
	contexto['imagenes']=ImagenProducto.objects.get(producto=id_pro)
	contexto["categorias"]=categorias
	if ofertas.filter(producto=id_pro).exists():
		obtener_oferta=ofertas.get(producto=producto.id_producto)
		precio_oferta=producto.precio-(obtener_oferta.porciento_desc*producto.precio)/100
		contexto['precio_oferta']=precio_oferta
		contexto['oferta']=ofertas.get(producto=id_pro)
		contexto['ahorra']=(obtener_oferta.porciento_desc*producto.precio)/100

	venta=Venta.objects.filter(cliente=request.user.id,estado_venta=1)    
	ventas_usuario=venta.values_list('id_venta')
	detallesventas_usuario=DetalleVenta.objects.filter(id_venta__in=ventas_usuario)
	puede_comentar=0
	if detallesventas_usuario.filter(producto=id_pro).exists():
		puede_comentar=1
	else:
		puede_comentar=0

	contexto['puede_comentar']=puede_comentar	


	return render(request,'tienda/producto.html',contexto)

class Comentarioo():
	id_usuario= ""
	nombre_usuario=""
	avatar=""
	id_producto=""
	id_comentario=""
	comentario=""
	fecha_comentario=""

def obtener_comentarioss(comentarios):
	lista_comentarios=[]
	for comentario in comentarios:
		obj_comentario=Comentarioo()
		obj_comentario.id_usuario=comentario.usuario.id
		usuarioo=User.objects.get(id=comentario.usuario.id)
		obj_comentario.nombre_usuario=usuarioo.get_username()
		try:
			cliente=Cliente.objects.get(usuario=comentario.usuario.id)
			obj_comentario.avatar=str(cliente.avatar)
		except Cliente.DoesNotExist:
			cliente = None
		obj_comentario.id_producto=comentario.producto.id_producto
		obj_comentario.id_comentario=comentario.id_comentario
		obj_comentario.comentario=comentario.comentario
		obj_comentario.fecha_comentario=str(comentario.fecha_comentario)

		ObjComentario=jsonpickle.encode(obj_comentario)
		lista_comentarios.append(ObjComentario)	
	return lista_comentarios	

def obtener_comentarios(request):
	id_producto=request.GET.get('id_producto', None)
	comentarios=Comentario.objects.filter(producto=id_producto).order_by('-id_comentario')
	lista_comentarios=obtener_comentarioss(comentarios)
	data={}
	data["comentarios"]=list(lista_comentarios)
	return JsonResponse(data,safe=False)

def hacer_comentario(request):
	comentario=Comentario()
	producto_comentario=request.GET.get('id_producto',None)
	
	if Comentario.objects.filter(usuario=request.user.id, producto=producto_comentario).exists():
		mensaje="Solo puedes comentar una vez por producto!"
		mensaje_success=0
	else:
		comentario.usuario=User.objects.get(id=request.user.id)
		comentario.producto=Producto.objects.get(id_producto=request.GET.get('id_producto',None))
		comentario.comentario=request.GET.get('comentario',None)
		comentario.fecha_comentario=hoy	
		comentario.save()
		mensaje="Gracias por haber comentado el producto!"
		mensaje_success=1
		
	data={}
	data['mensaje']=mensaje
	data['exito']=mensaje_success
	return JsonResponse(data,safe=False)

def editar_comentario(request):
	id_comentario=request.GET.get('id_comentario',None)
	comentario=Comentario.objects.get(id_comentario=id_comentario)
	comentario.comentario=request.GET.get('comentario',None)
	comentario.save()
	data={}
	data['mensaje_actualizar']="Comentario editado con exito"
	return JsonResponse(data,safe=False)

#sdljkasdajslkjdlkakl






#Obtener productos especificos
def obtener_determinados_productos(request):
	categoria=request.GET.get('categoria',None)
	id_productos=[]
	marcass=request.GET.get('marcas', None)
   
	marcas=json.loads(marcass)
	
   
	if categoria== "1":
		familiass=request.GET.get('familias',None)	
		socketss=request.GET.get('sockets',None)
		coress=request.GET.get('cores',None)

		familias=json.loads(familiass)
		sockets=json.loads(socketss)
		cores=json.loads(coress)

		productos_procesadores=Procesador.objects.none()
		lista_familias=Procesador.objects.none()
		lista_sockets=Procesador.objects.none()
		lista_cores=Procesador.objects.none()

		if familias:
			lista_familias=Procesador.objects.filter(familia_procesador__in=familias)
		if sockets:
			lista_sockets=Procesador.objects.filter(socket_procesador__in=sockets)
		if cores:
			lista_cores=Procesador.objects.filter(nucleos__in=cores)

		productos_procesadores=lista_familias|lista_sockets|lista_cores	
			
		if productos_procesadores:	
			id_productos=productos_procesadores.values_list('producto',flat=True)

	elif categoria=="2":
		familiass=request.GET.get('familias',None)	
		procesadoresgraficoss=request.GET.get('procesadoresgraficos',None)
		memoriass=request.GET.get('memorias',None)
		tiposs=request.GET.get('tipos',None)

		familias=json.loads(familiass)
		procesadoresgraficos=json.loads(procesadoresgraficoss)
		memorias=json.loads(memoriass)
		tipos=json.loads(tiposs)
		

		productos_graficas=TarjetaVideo.objects.none()
		lista_familias=TarjetaVideo.objects.none()
		lista_procesadoresgraficos=TarjetaVideo.objects.none()
		lista_memorias=TarjetaVideo.objects.none()
		lista_tipos=TarjetaVideo.objects.none()

		if familias:
			lista_familias=TarjetaVideo.objects.filter(familia_grafica__in=familias)
		if procesadoresgraficos:
			lista_procesadoresgraficos=TarjetaVideo.objects.filter(procesador_grafico__in=procesadoresgraficos)
		if memorias:
			lista_memorias=TarjetaVideo.objects.filter(memoria_grafica_gb__in=memorias)
		if tipos:
			lista_tipos=TarjetaVideo.objects.filter(tipo_memoria_grafica__in=tipos)

		productos_graficas= lista_familias|lista_procesadoresgraficos|lista_memorias|lista_tipos


		if productos_graficas:	
			id_productos=productos_graficas.values_list('producto',flat=True)

	if categoria=="3":
		familiass=request.GET.get('familias',None)
		socketss=request.GET.get('sockets',None)
		chipsetss=request.GET.get('chipsets',None)
		memoriass=request.GET.get('memorias',None)
		tiposs=request.GET.get('tipos',None)
		formass=request.GET.get('formas',None)
		parass=request.GET.get('paras',None)

		familias=json.loads(familiass)
		sockets=json.loads(socketss)
		chipsets=json.loads(chipsetss)
		memorias=json.loads(memoriass)
		tipos=json.loads(tiposs)
		formas=json.loads(formass)
		paras=json.loads(parass)
	

		productos_mobos=TarjetaMadre.objects.none()
		lista_familias=TarjetaMadre.objects.none()
		lista_sockets=TarjetaMadre.objects.none()
		lista_chipsets=TarjetaMadre.objects.none()
		lista_memorias=TarjetaMadre.objects.none()
		lista_tipos=TarjetaMadre.objects.none()
		lista_formas=TarjetaMadre.objects.none()
		lista_paras=TarjetaMadre.objects.none()

		if familias:
			lista_familias=TarjetaMadre.objects.filter(familia_procesador__in=familias)
		if sockets:
			lista_sockets=TarjetaMadre.objects.filter(socket_procesador__in=sockets)
		if chipsets:
			lista_chipsets=TarjetaMadre.objects.filter(chipset__in=chipsets)
		if memorias:
			lista_memorias=TarjetaMadre.objects.filter(cantidad_memoria_gb__in=memorias)
		if tipos:
			lista_tipos=TarjetaMadre.objects.filter(tipo_memoria__in=tipos)
		if formas:
			lista_formas=TarjetaMadre.objects.filter(factor_forma__in=formas)
		if paras:
			lista_paras=TarjetaMadre.objects.filter(para_marca__in=paras)

		productos_mobos=(lista_familias|lista_sockets|lista_chipsets|lista_memorias|lista_tipos|lista_formas|lista_paras)

		if productos_mobos:
			id_productos=productos_mobos.values_list('producto',flat=True)

	if categoria=="4":
		capacidadess=request.GET.get('capacidades',None)
		interfacess=request.GET.get('interfaces',None)
		capacidades=json.loads(capacidadess)
		interfaces=json.loads(interfacess)
		productos_ssd=SSD.objects.none()
		lista_capacidades=SSD.objects.none()
		lista_interfaces=SSD.objects.none()
		if capacidades:
			lista_capacidades=SSD.objects.filter(capacidad__in=capacidades)
		if interfacess:
			lista_interfaces=SSD.objects.filter(interfazdd__in=interfaces)

		productos_ssd=lista_capacidades|lista_interfaces

		if productos_ssd:
			id_productos=productos_ssd.values_list('producto',flat=True)

	if categoria=="5":
		capacidadess=request.GET.get('capacidades',None)
		interfacess=request.GET.get('interfaces',None)
		cachess=request.GET.get('caches',None)
		rpmss=request.GET.get('rpms',None)
		tamddss=request.GET.get('tamdds',None)
		capacidades=json.loads(capacidadess)
		interfaces=json.loads(interfacess)
		caches=json.loads(cachess)
		rpms=json.loads(rpmss)
		tamdds=json.loads(tamddss)
		productos_dds=DiscoDuro.objects.none()
		lista_capacidades=DiscoDuro.objects.none()
		lista_interfaces=DiscoDuro.objects.none()
		lista_caches=DiscoDuro.objects.none()
		lista_rpms=DiscoDuro.objects.none()
		lista_tamdds=DiscoDuro.objects.none()

		if capacidades:
			lista_capacidades=DiscoDuro.objects.filter(capacidad__in=capacidades)
		if interfaces:
			lista_interfaces=DiscoDuro.objects.filter(interfazdd__in=interfaces)
		if caches:
			lista_caches=DiscoDuro.objects.filter(cache__in=caches)
		if rpms:
			lista_rpms=DiscoDuro.objects.filter(rpm__in=rpms)
		if tamdds:
			lista_tamdds=DiscoDuro.objects.filter(tamdd__in=tamdds)

		productos_dds=lista_capacidades|lista_interfaces|lista_caches|lista_rpms|lista_tamdds
		if productos_dds:
			id_productos=productos_dds.values_list('producto',flat=True)

	elif categoria=="6":
		gbss=request.GET.get('gbs',None)
		mhzss=request.GET.get('mhzs',None)
		tiposs=request.GET.get('tipos',None)
		formass=request.GET.get('formas',None)
		gbs=json.loads(gbss)
		mhzs=json.loads(mhzss)
		tipos=json.loads(tiposs)
		formas=json.loads(formass)
		productos_rams=RAM.objects.none()
		lista_gbs=RAM.objects.none()
		lista_mhzs=RAM.objects.none()
		lista_tipos=RAM.objects.none()
		lista_formas=RAM.objects.none()

		if gbs:
			lista_gbs=RAM.objects.filter(cantidad_memoria_gb__in=gbs)
		if mhzs:
			lista_mhzs=RAM.objects.filter(cantidad_memoria_mhz__in=mhzs)
		if tipos:
			lista_tipos=RAM.objects.filter(tipo_memoria__in=tipos)
		if formas:
			lista_formas=RAM.objects.filter(factor_forma_ram__in=formas)
		productos_rams=lista_gbs|lista_mhzs|lista_tipos|lista_formas

		if productos_rams:
			id_productos=productos_rams.values_list('producto',flat=True)

	elif categoria=="7":
		potenciass=request.GET.get('potencias',None)
		certificacioness=request.GET.get('certificaciones',None)
		formass=request.GET.get('formas',None)
		potencias=json.loads(potenciass)
		certificaciones=json.loads(certificacioness)
		formas=json.loads(formass)

		productos_psus=PSU.objects.none()
		lista_potencias=PSU.objects.none()
		lista_certificaciones=PSU.objects.none()
		lista_formas=PSU.objects.none()

		if potencias:
			lista_potencias=PSU.objects.filter(potencia_nominal__in=potencias)
		if certificaciones:
			lista_certificaciones=PSU.objects.filter(certificacion__in=certificaciones)
		if formas:
			lista_formas=PSU.objects.filter(factor_forma__in=formas)

		productos_psus=lista_potencias|lista_certificaciones|lista_formas
		if productos_psus:
			id_productos=productos_psus.values_list('producto',flat=True)

	elif categoria=="8":
		formass=request.GET.get('formas',None)
		formas=json.loads(formass)
		lista_formas=Gabinete.objects.none()
		productos_gabos=Gabinete.objects.none()

		if formas:
			lista_formas=Gabinete.objects.filter(factor_forma_gabinete__in=formas)
		productos_gabos=lista_formas
		if productos_gabos:
			id_productos=productos_gabos.values_list('producto',flat=True)

	elif categoria=="9":
		conectividadess=request.GET.get('conectividades',None)
		conectividades=json.loads(conectividadess)
		print(conectividades)
		productos_teclado=Teclado.objects.none()
		lista_conectividades=Teclado.objects.none()
		if conectividades:
			lista_conectividades=Teclado.objects.filter(conectividad__in=conectividades)
		productos_teclado=lista_conectividades
		if productos_teclado:
			id_productos=productos_teclado.values_list('producto',flat=True)

	elif categoria=="10":
		conectividadess=request.GET.get('conectividades',None)
		conectividades=json.loads(conectividadess)
		productos_mouse=Mouse.objects.none()
		lista_conectividades=Mouse.objects.none()
		if conectividades:		
			lista_conectividades=Mouse.objects.filter(conectividad__in=conectividades)
		productos_mouse=lista_conectividades
		if productos_mouse:
			id_productos=productos_mouse.values_list('producto',flat=True)
	elif categoria=="11":
		resolucioness=request.GET.get('resoluciones',None)
		pantallass=request.GET.get('pantallas',None)
		puertoss=request.GET.get('puertos',None)
		resoluciones=json.loads(resolucioness)
		pantallas=json.loads(pantallass)
		puertos=json.loads(puertoss)
		productos_monitores=Monitor.objects.none()
		lista_resoluciones=Monitor.objects.none()
		lista_pantallas=Monitor.objects.none()
		lista_puertos=Monitor.objects.none()
		lista_puertos_hdmi=Monitor.objects.none()
		lista_puertos_dvi=Monitor.objects.none()
		lista_puertos_dp=Monitor.objects.none()
		lista_puertos_vga=Monitor.objects.none()

		if pantallas:
			lista_pantallas=Monitor.objects.filter(tam_pantalla__in=pantallas)
		if resoluciones:
			lista_resoluciones=Monitor.objects.filter(resolucion__in=resoluciones)
		if puertos:
			for puerto in puertos:
				print(puerto)
				if puerto=="1":
					print("entré hdmi")
					lista_puertos_hdmi=Monitor.objects.filter(cantidad_hdmi__gte=1)
				elif puerto=="2":
					lista_puertos_dvi=Monitor.objects.filter(cantidad_dvi__gt=1)
				elif puerto=="3":
					print("entré dp")
					lista_puertos_dp=Monitor.objects.filter(cantidad_dp__gte=1)
				elif puerto=="4":
					lista_puertos_vga=Monitor.objects.filter(cantidad_vga__gte=1)
			lista_puertos=lista_puertos_hdmi|lista_puertos_vga|lista_puertos_dvi|lista_puertos_dp
		productos_monitores=lista_pantallas|lista_resoluciones|lista_puertos
		if productos_monitores:
			id_productos=productos_monitores.values_list('producto',flat=True)




	if  marcas:
		productos=Producto.objects.filter(Q(id_producto__in=id_productos ,estado_producto="A", cantidad__gte=1,categoria=categoria)|Q(marca__in=marcas,categoria=categoria))
	else:
		if id_productos:
			productos=Producto.objects.filter(id_producto__in=id_productos, estado_producto="A", cantidad__gte=1,categoria=categoria)
		   
		else:
			productos=Producto.objects.filter(estado_producto="A", cantidad__gte=1,categoria=categoria)

	lista_productos=obtener_productos2(productos)
	cantidad_productos=len(lista_productos)
	
	data={}
	data['productos']=list(lista_productos)
	data['cantidad']=cantidad_productos
	return JsonResponse(data,safe=False)

def obtener_productos_por_categoria(request):
	id_categoria=request.GET.get('id_categoria',None)
	productos=Producto.objects.filter(categoria=id_categoria, cantidad__gte=1, estado_producto="A")
	lista_productos=obtener_productos2(productos)
	cantidad_productos=len(lista_productos)
	data={}
	data['productos']=list(lista_productos)
	data['cantidad']=cantidad_productos
	return JsonResponse(data,safe=False)

def obtener_total_carrito(request):
	lista_productos_carrito2=request.GET.get('lista_productos_carrito',None)
	lista_productos_carrito=json.loads(lista_productos_carrito2)
	lista_productos_carrito=lista_productos_carrito.split(",")
	total_carrito=0
	for producto in lista_productos_carrito:
		if producto!="":
			if ofertas.filter(producto=producto).exists():
				producto2=productos.get(id_producto=producto)
				obtener_oferta=ofertas.get(producto=producto)
				precio_oferta=producto2.precio-(obtener_oferta.porciento_desc*producto2.precio)/100
				total_carrito=total_carrito+precio_oferta
			else:
				producto_carrito=productos.get(id_producto=producto)
				total_carrito=total_carrito+producto_carrito.precio
	print(lista_productos_carrito)				
	print(len(lista_productos_carrito))
	data={}
	data["total"]=total_carrito
	data["cantidad"]=len(lista_productos_carrito)
	return JsonResponse(data,safe=False)

def obtener_cantidad_favorito(request):
	lista_productos_favorito2=request.GET.get('lista_productos_favorito',None)
	lista_productos_favorito=json.loads(lista_productos_favorito2)
	lista_productos_favorito=set(lista_productos_favorito.split(","))

	data={}
	data["cantidad"]=len(lista_productos_favorito)
	return JsonResponse(data,safe=False)

class ObjetoCarrito():
	id_producto=""
	cantidad=""
	total=""

def ver_carrito(request):
	lista_productos_carrito2=request.GET.get('lista_productos_carrito',None)
	lista_productos_carrito=json.loads(lista_productos_carrito2)
	lista_productos_carrito=lista_productos_carrito.split(",")
	productos_carrito=productos.filter(id_producto__in=lista_productos_carrito)
	productos_a_comprar=obtener_productos2(productos_carrito)
	solo_productos=set(lista_productos_carrito)
	lista_cantidades=[]
	for producto in solo_productos:
		objeto_carro=ObjetoCarrito()
		objeto_carro.cantidad=lista_productos_carrito.count(producto)
		objeto_carro.id_producto=producto
		ObjProducto=jsonpickle.encode(objeto_carro)
		lista_cantidades.append(ObjProducto)

	total_carrito=0
	for producto in lista_productos_carrito:
		if producto!="":
			if ofertas.filter(producto=producto).exists():
				producto2=productos.get(id_producto=producto)
				obtener_oferta=ofertas.get(producto=producto)
				precio_oferta=producto2.precio-(obtener_oferta.porciento_desc*producto2.precio)/100
				total_carrito=total_carrito+precio_oferta
			else:
				producto_carrito=productos.get(id_producto=producto)
				total_carrito=total_carrito+producto_carrito.precio
	print(total_carrito)
	print(len(productos_a_comprar))
	data={}
	data["total"]=total_carrito
	data['productos']=productos_a_comprar
	data['cantidades']=lista_cantidades
	data['cantidad']=len(productos_a_comprar)
	return JsonResponse(data,safe=False)

def obtener_total_carrito2(productos_carrito):
	total_carrito=0
	for producto in productos_carrito:
		if producto!="":
			if ofertas.filter(producto=producto).exists():
				producto2=productos.get(id_producto=producto)
				obtener_oferta=ofertas.get(producto=producto)
				precio_oferta=producto2.precio-(obtener_oferta.porciento_desc*producto2.precio)/100
				total_carrito=total_carrito+precio_oferta
			else:
				producto_carrito=productos.get(id_producto=producto)
				total_carrito=total_carrito+producto_carrito.precio
	data={}
	data["total"]=total_carrito
	data["cantidad"]=len(productos_carrito)
	return data

def obtener_listado_favoritos(request):
	listado_favoritos_locales=json.loads(request.GET.get('listado_favoritos_locales',None))
	listado_favoritos_servidor=Favorito.objects.filter(cliente=request.user.id)
	cliente=Cliente.objects.get(usuario=request.user.id)
	if listado_favoritos_locales:

		l=listado_favoritos_locales[0].split(',')
		for producto_favorito in l:
			if producto_favorito!="":
				if listado_favoritos_servidor.filter(producto=Producto.objects.get(id_producto=producto_favorito)).exists():
					print("Ya está en sus favoritos")
				else:
					Favorito.objects.create(cliente=cliente,producto=Producto.objects.get(id_producto=producto_favorito))
	listado_favoritos=Favorito.objects.filter(cliente=cliente)
	favoritos=listado_favoritos.values_list('producto',flat=True)
	favoritos_productos=productos.filter(id_producto__in=favoritos)
	data={}
	data['listado_favoritos']=obtener_productos2(favoritos_productos)
	return JsonResponse(data,safe=False)

def eliminar_de_favoritos(request):
	producto_a_eliminar=request.GET.get('producto_favorito_eliminar',None)
	cliente=Cliente.objects.get(usuario=request.user.id)
	producto2=productos.get(id_producto=producto_a_eliminar)
	favoritos=Favorito.objects.get(cliente=cliente,producto=producto2)
	favoritos.delete()
	listado_favoritos=Favorito.objects.filter(cliente=cliente)
	favoritos2=listado_favoritos.values_list('producto',flat=True)
	favoritos_productos=productos.filter(id_producto__in=favoritos2)
	data={}
	data['cantidad']=len(favoritos_productos)
	data['listado_favoritos']=obtener_productos2(favoritos_productos)
	return JsonResponse(data,safe=False)

from reportlab.platypus import Image, Paragraph, Table,TableStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
class factura_compra_pdf(View):

	def cabecera(self,pdf):
		#Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
		archivo_imagen = settings.MEDIA_ROOT+'/logo_factura/dimercom-factura.jpg'
		print(archivo_imagen)
		#Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
		pdf.drawImage(archivo_imagen, 40, 720, 150, 100,preserveAspectRatio=True)

		#Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
		pdf.setFont("Helvetica", 16)
		#Dibujamos una cadena en la ubicación X,Y especificada
		pdf.drawString(230, 700, u"Facturacion")
		pdf.setFont("Helvetica", 14)
		pdf.drawString(200, 680, u"Carrito de compras "+ self.kwargs['slug'])
		pdf.setFont("Helvetica", 10)
		pdf.drawString(400,800,u"DIMERCOM - computo inteligente -")
		pdf.drawString(400,790,u"Av. 31 Poniente 109 Local B")
		pdf.drawString(400,780,u"Colonia Chulavista")
		pdf.drawString(400,770,u"Puebla,Pue")
		pdf.drawString(400,760,u"C.p:72420")
		pdf.drawString(400,750,u"Company ID: dimercom.mx")
		pdf.drawString(400,740,u"Telephone: 012222460007")
		pdf.drawString(400,730,u"Email: info@dimercom.mx")


		detalle=total_factura(self.kwargs['slug'])
		pdf.setFont("Helvetica", 16)
		pdf.drawString(400,300,u"Subtotal: $"+detalle.total_sin_iva)
		pdf.drawString(400,280,u"Iva: $"+detalle.iva)
		pdf.drawString(400,260,u"Envio: $" +str(detalle.envio))
		pdf.drawString(400,240,u"Total: $"+str(float(detalle.envio)+float(detalle.total)))
		

	def get(self, request, *args, **kwargs):
		#Indicamos el tipo de contenido a devolver, en este caso un pdf
		response = HttpResponse(content_type='application/pdf')
		#La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
		buffer = BytesIO()
		#Canvas nos permite hacer el reporte con coordenadas X y Y
		pdf = canvas.Canvas(buffer)
		#Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
		self.cabecera(pdf)
		y=600
		z=400
		self.tabla_informacion(pdf, y,request)
		self.tabla_productos(pdf, z,request)
		#Con show page hacemos un corte de página para pasar a la siguiente
		pdf.showPage()
		pdf.save()
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response

	def tabla_informacion(self,pdf,y,request):
		encabezados = ('Venta #', 'Id Cliente','Metodo de pago','Fecha de venta',  )
		#Creamos una lista de tuplas que van a contener a las personas
		venta=Venta.objects.get(id_venta=self.kwargs['slug'])
		
		
		detalles = [(venta.id_venta, request.user.id, venta.tipo_pago.tipo_pago,venta.fecha_venta)]
		#Establecemos el tamaño de cada una de las columnas de la tabla
		detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 2 * cm,  3 * cm,3 * cm])
		#Aplicamos estilos a las celdas de la tabla
		detalle_orden.setStyle(TableStyle(
		[
				#La primera fila(encabezados) va a estar centrada
				('ALIGN',(0,0),(3,0),'CENTER'),
				#Los bordes de todas las celdas serán de color negro y con un grosor de 1
				('GRID', (0, 0), (-1, -1), 1, colors.black),
				#El tamaño de las letras de cada una de las celdas será de 10
				('FONTSIZE', (0, 0), (-1, -1), 10),
				('TEXTCOLOR',(1,1),(0,1),"#337ab7"),
				]
		))
		#Establecemos el tamaño de la hoja que ocupará la tabla
		detalle_orden.wrapOn(pdf, 800, 600)
		#Definimos la coordenada donde se dibujará la tabla
		detalle_orden.drawOn(pdf, 60,y)



	def tabla_productos(self,pdf,z,request):
		encabezados = ('Producto #', 'Imagen','Descripcion','Cantidad','precio'  )
		#Creamos una lista de tuplas que van a contener a las personas
		detalle_venta=DetalleVenta.objects.filter(id_venta=self.kwargs['slug'])
		#imagenes=ImagenProducto.objects.get(id_producto=detalle.producto.id_producto)
		#imagen=imagenes.imagen_principal
		def obtenerimagen(id_producto):
			imagen=ImagenProducto.objects.get(producto=id_producto)
			imagenn=imagen.imagen_principal
			imagennn=imagenn.url
			a = Image(settings.MEDIA_ROOT+imagennn[6:])  
			a.drawHeight = 1.5*cm
			a.drawWidth = 1.5*cm
			#pdf.drawImage(settings.MEDIA_ROOT+imagennn[6:], 40, 750, 120, 90,preserveAspectRatio=True) 
#data=[['1',a],['3','4']]
			return a #settings.MEDIA_ROOT+imagennn[6:]
			
		
		detalles = [(detalle.producto.id_producto,obtenerimagen(detalle.producto.id_producto) ,obtenerDescripcionProducto(request,detalle.producto.id_producto), detalle.cantidad,detalle.precio) for detalle in detalle_venta ] 
		#Establecemos el tamaño de cada una de las columnas de la tabla
		detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 2 * cm,  8 * cm,1.5 * cm, 2* cm])
		#Aplicamos estilos a las celdas de la tabla
		detalle_orden.setStyle(TableStyle(
		[
				#La primera fila(encabezados) va a estar centrada
				('ALIGN',(0,0),(3,0),'CENTER'),
				#Los bordes de todas las celdas serán de color negro y con un grosor de 1
				('GRID', (0, 0), (-1, -1), 1, colors.black),
				#El tamaño de las letras de cada una de las celdas será de 10
				('FONTSIZE', (0, 0), (-1, -1), 10),
				]
		))
		#Establecemos el tamaño de la hoja que ocupará la tabla
		detalle_orden.wrapOn(pdf, 800, 600)
		#Definimos la coordenada donde se dibujará la tabla
		detalle_orden.drawOn(pdf, 60,z)	

class NombreProducto:
	id_producto=""
	descripcion=""
	imagen=""

def obtenerDescripcionProducto(request,id_producto=None,q=None):
	q=request.GET.get('q',None)
	#producto=Producto.objects.get(id_producto=id_producto)
	#imagenes=ImagenProducto.objects.get(producto=id_producto)
	#nombre_producto.id_producto=id_producto
	#nombre_producto.imagen=str(imagenes.imagen_principal) 
	#categoria=categorias.objects.get(id_categoria=producto.categoria.id_categoria).values('categoria')
	#if producto.categoria.id_categoria==1:
	#	nombre_producto.descripcion= categoria
	descripciones=[]
	productos=Producto.objects.filter(estado_producto="A", cantidad__gte=1)
	for producto in productos:
		nombre_producto=NombreProducto()
		imagenes=ImagenProducto.objects.get(producto=producto.id_producto)
		imagen2=imagenes.imagen_principal
		imagen=imagen2.url
		nombre_producto.id_producto=str(producto.id_producto)
		nombre_producto.imagen=imagen[6:]
		categoria=Categoria.objects.get(id_categoria=producto.categoria.id_categoria)
		categoria_nombre=categoria.categoria
		marca=Marca.objects.get(id_marca=producto.marca.id_marca)
		marca_nombre=marca.marca
		descripcion=""
		descripcion=categoria_nombre + " " + marca_nombre
		
		if categoria.id_categoria==1:
			subproducto=Procesador.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.familia_procesador.familia_procesador + " "+ subproducto.modelo_procesador.modelo_procesador
		elif categoria.id_categoria==2:
			subproducto=TarjetaVideo.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.familia_grafica.familia_grafica + " "+ subproducto.procesador_grafico.procesador_grafico +" "+ subproducto.modelo_grafica.modelo_grafica
		elif categoria.id_categoria==3:
			subproducto=TarjetaMadre.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.factor_forma.factor_forma + " "+ subproducto.chipset.chipset +" "+ subproducto.modelo_tarjeta_madre.modelo_tarjeta_madre
		elif categoria.id_categoria==4:
			subproducto=SSD.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_dd.modelo_dd + " "+ str(subproducto.capacidad)+"GB"
		elif categoria.id_categoria==5:
			subproducto=DiscoDuro.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_dd.modelo_dd + " "+ str(subproducto.capacidad)+"GB"
		elif categoria.id_categoria==6:
			subproducto=RAM.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_ram.modelo_ram + " "+ str(subproducto.cantidad_memoria_gb)+" "+subproducto.tipo_memoria.tipo_memoria
		elif categoria.id_categoria==7:
			subproducto=PSU.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_psu.modelo_psu + " "+ str(subproducto.potencia_nominal)+"W "+subproducto.certificacion.certificacion
		elif categoria.id_categoria==8:
			subproducto=Gabinete.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_gabinete.modelo_gabinete + " "+ subproducto.factor_forma_gabinete.factor_forma_gabinete
		elif categoria.id_categoria==9:
			subproducto=Teclado.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_teclado.modelo_teclado
		elif categoria.id_categoria==10:
			subproducto=Mouse.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_mouse.modelo_mouse +" " +str(subproducto.dpi)+" dpi"
		elif categoria.id_categoria==11:
			subproducto=Monitor.objects.get(producto=producto.id_producto)
			descripcion=descripcion + " "+ subproducto.modelo_monitor.modelo_monitor +" "+str(subproducto.tam_pantalla)+" pulgadas "+subproducto.resolucion.resolucion

		nombre_producto.descripcion=descripcion
		
		descripciones.append(nombre_producto)
	if id_producto!="":
		for descripcion in descripciones:
			if descripcion.id_producto==str(id_producto):
				return descripcion.descripcion

	productos_busqueda=[]				
	if q!="" and q!=" ":

		for descripcion in descripciones:
			if q.lower() in descripcion.descripcion.lower():
				productos_busqueda.append(jsonpickle.encode(descripcion))
		data={}
		data["resultados"]=len(productos_busqueda)		
		data['busqueda_productos']=productos_busqueda
		return JsonResponse(data,safe=False)
	return ""
		


class TotalDetalleVenta():
	id_venta=""
	total=""
	total_sin_iva=""
	iva=""
	envio=""
def total_factura(id_venta):
	detalles_ventas=DetalleVenta.objects.filter(id_venta=id_venta)
	total=0
	for detalle_venta in detalles_ventas:
		total=total+(detalle_venta.cantidad*detalle_venta.precio)

	totaldetalles=TotalDetalleVenta()
	totaldetalles.id_venta=str(id_venta)
	totaldetalles.total=str(total)
	totaldetalles.iva=str(total*0.16)
	totaldetalles.total_sin_iva=str(total-(total*0.16))
	totaldetalles.envio="150"
	return totaldetalles

def verificar_producto(request):
	id_producto=request.GET.get('id_producto',None)
	cantidad_comprar=request.GET.get('cantidad_comprar',None)
	print(id_producto)
	producto=productos.get(id_producto=id_producto)
	print(producto)
	cantidad=producto.cantidad
	if cantidad_comprar<=str(cantidad):
		mensaje="puede comprar"
		bandera=1
	else:
		mensaje="no pude comprar"
		bandera=0
	data={}
	data['bandera']=bandera
	data['mensaje']=mensaje

	return JsonResponse(data,safe=False)









