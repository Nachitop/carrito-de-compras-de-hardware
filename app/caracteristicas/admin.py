# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#Procesador
from app.caracteristicas.models import FamiliaProcesador, ModeloProcesador, SocketProcesador, CacheProcesador, Litografia, SO, TipoMemoria, PesoYDimension, ProcesadorGrafico, TipoInterfaz, FamiliaGrafica, TipoMemoriaGrafica, Color, ModeloGrafica
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
# Register your models here.

admin.site.register(Color)


#Procesador
admin.site.register(FamiliaProcesador)
admin.site.register(ModeloProcesador)
admin.site.register(SocketProcesador)
admin.site.register(CacheProcesador)
admin.site.register(Litografia)
admin.site.register(SO)
admin.site.register(TipoMemoria)
admin.site.register(PesoYDimension)
#Tarjetavideo
admin.site.register(ProcesadorGrafico)
admin.site.register(TipoInterfaz)
admin.site.register(FamiliaGrafica)
admin.site.register(TipoMemoriaGrafica)
admin.site.register(ModeloGrafica)

#DD y SSD
admin.site.register(RPM)
admin.site.register(TamDD)
admin.site.register(InterfazDD)
admin.site.register(ModeloDD)

#RAM
admin.site.register(FactorFormaRAM)
admin.site.register(ModeloRAM)

#PSU
admin.site.register(FactorForma)
admin.site.register(Certificacion)
admin.site.register(ModeloPSU)

#TarjetaMadre
admin.site.register(Chipset)
admin.site.register(ModeloTarjetaMadre)

#Gabinete
admin.site.register(ModeloGabinete)
admin.site.register(FactorFormaGabinete)

#Teclado
admin.site.register(ModeloTeclado)
admin.site.register(Conectividad)
admin.site.register(Idioma)

#Mouse
admin.site.register(ModeloMouse)

#Monitor
admin.site.register(ModeloMonitor)
admin.site.register(RelacionAspecto)
admin.site.register(HD)
admin.site.register(Resolucion)





	