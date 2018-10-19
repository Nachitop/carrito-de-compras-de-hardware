# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.cliente.models import Cliente, DomicilioCliente, Favorito

#Register your models here.
admin.site.register(Cliente)
admin.site.register(DomicilioCliente)
admin.site.register(Favorito)