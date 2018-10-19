# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.subproducto.models import Procesador,TarjetaVideo, TarjetaMadre, DiscoDuro, SSD,RAM, PSU, Gabinete, Teclado, Mouse, Monitor

# Register your models here.
admin.site.register(Procesador)
admin.site.register(TarjetaVideo)
admin.site.register(TarjetaMadre)
admin.site.register(DiscoDuro)
admin.site.register(SSD)
admin.site.register(RAM)
admin.site.register(PSU)
admin.site.register(Gabinete)
admin.site.register(Teclado)
admin.site.register(Mouse)
admin.site.register(Monitor)
