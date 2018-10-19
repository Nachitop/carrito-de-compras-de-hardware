# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.producto.models import Categoria, Producto, ImagenProducto, Marca, Comentario

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(ImagenProducto)
admin.site.register(Marca)
admin.site.register(Comentario)
