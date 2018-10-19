# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.venta.models import Venta, DetalleVenta, EstadoVenta, Oferta, TipoPago

# Register your models here.
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Oferta)
admin.site.register(EstadoVenta)
admin.site.register(TipoPago)


