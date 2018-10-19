# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from app.tienda.views import *
# Create your views here.


ventas=Venta.objects.all()
detalle_ventas=DetalleVenta.objects.all()
productos_carrito=[]





def recibir_carrito(request):
    lista_productos_carrito2=request.GET.get('lista_productos_carrito',None)
    lista_productos_carrito=json.loads(lista_productos_carrito2)
    global productos_carrito 
    productos_carrito=lista_productos_carrito.split(",")
    data={}
    data['mensaje']="enviado correctamente"
    return JsonResponse(data,safe=False)




@csrf_exempt
def payment_done(request):
	categorias=Categoria.objects.all().order_by("categoria")
	contexto= {'categorias': categorias}
	ventas_actual=ventas.filter(cliente=request.user.id,fecha_venta=hoy).last()
	estado_venta=EstadoVenta.objects.get(id_estado_venta=1)
	ventas_actual.estado_venta=estado_venta
	ventas_actual.save()
	return render(request,'pagos/done.html',contexto)
@csrf_exempt	
def payment_canceled(request):
	categorias=Categoria.objects.all().order_by("categoria")
	contexto= {'categorias': categorias}
	ventas_actual=ventas.filter(cliente=request.user.id,fecha_venta=hoy, estado_venta=2).last()
	estado_venta=EstadoVenta.objects.get(id_estado_venta=3)
	ventas_actual.estado_venta=estado_venta
	ventas_actual.save()
	return render(request,'pagos/canceled.html',contexto)

@csrf_exempt
def payment_process(request):
    global productos_carrito
    data_retornada=obtener_total_carrito2(productos_carrito)
    total_carrito= data_retornada['total']
    solo_productos=set(productos_carrito)
    print("solo_productos")
    print(solo_productos)
    lista_cantidades=[]
    for producto in solo_productos:
        objeto_carro=ObjetoCarrito()
        objeto_carro.cantidad=productos_carrito.count(producto)
        objeto_carro.id_producto=producto
        lista_cantidades.append(objeto_carro)
        print("objetos en carro")
        print(producto)


    ventas.create(cliente=Cliente.objects.get(usuario=request.user.id),tipo_pago=TipoPago.objects.get(id_tipo_pago=1),fecha_venta=hoy,estado_venta=EstadoVenta.objects.get(id_estado_venta=2))

    for producto in solo_productos:
    	cantidad=0
    	precio=0
    	for producto2 in lista_cantidades:
    		if producto2.id_producto == producto:
    			cantidad=producto2.cantidad
        if ofertas.filter(producto=producto).exists():
            producto3=productos.get(id_producto=producto)
            obtener_oferta=ofertas.get(producto=producto)
            precio_oferta=producto3.precio-(obtener_oferta.porciento_desc*producto3.precio)/100
            precio=precio_oferta
        else:
            producto_carrito=productos.get(id_producto=producto2.id_producto)
            precio=producto_carrito.precio		
           
        detalle_ventas.create(id_venta=ventas.filter(cliente=request.user.id,fecha_venta=hoy).last(),producto=Producto.objects.get(id_producto=producto),cantidad=cantidad,precio=precio)


    id_venta=ventas.filter(cliente=request.user.id,fecha_venta=hoy).last()
    host = request.get_host()
    paypal_dict = {
    'business': settings.PAYPAL_RECEIVER_EMAIL,
    'amount': total_carrito,
    'shipping': '150',
    'item_name': 'Carrito Compras Dimercom',
    'invoice': id_venta,
    'currency_code': 'MXN',
    'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
    'return_url': 'http://{}{}'.format(host, reverse('pagos:done')),
    'cancel_return': 'http://{}{}'.format(host,reverse('pagos:canceled')),
    }
    paypaal = PayPalPaymentsForm(initial=paypal_dict)
    print(paypaal)
    contexto={}
    contexto['form']=paypaal
    return render(request, 'pagos/process.html', contexto)
