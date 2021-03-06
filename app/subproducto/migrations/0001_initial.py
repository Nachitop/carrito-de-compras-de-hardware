# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-09 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caracteristicas', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscoDuro',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('capacidad', models.PositiveIntegerField()),
                ('cache', models.PositiveIntegerField()),
                ('interfazdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.InterfazDD')),
                ('modelo_dd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloDD')),
                ('rpm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.RPM')),
                ('tamdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TamDD')),
            ],
        ),
        migrations.CreateModel(
            name='Gabinete',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('psu_incluida', models.BooleanField()),
                ('potencia_nominal', models.PositiveIntegerField(blank=True, null=True)),
                ('cantidad_puertos_usb2', models.PositiveIntegerField()),
                ('cantidad_puertos_usb3', models.PositiveIntegerField()),
                ('cantidad_ranuras_expansion', models.PositiveIntegerField()),
                ('cantidad_ventiladores', models.PositiveIntegerField()),
                ('ventana_lateral', models.BooleanField()),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('dd_soportados', models.ManyToManyField(to='caracteristicas.TamDD')),
                ('factor_forma_gabinete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.FactorFormaGabinete')),
                ('mobos_soportadas', models.ManyToManyField(to='caracteristicas.FactorForma')),
                ('modelo_gabinete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloGabinete')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('tam_pantalla', models.FloatField()),
                ('cantidad_hdmi', models.PositiveIntegerField()),
                ('cantidad_dvi', models.PositiveIntegerField()),
                ('cantidad_vga', models.PositiveIntegerField()),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('hd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.HD')),
                ('modelo_monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloMonitor')),
                ('relacion_aspecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.RelacionAspecto')),
                ('resolucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Resolucion')),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('dpi', models.PositiveIntegerField()),
                ('rgb', models.BooleanField()),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('conectividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Conectividad')),
                ('modelo_mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloMouse')),
                ('tipo_interfaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoInterfaz')),
            ],
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('frecuencia_mhz', models.FloatField()),
                ('frecuencia_turbo_mhz', models.FloatField()),
                ('disipador', models.BooleanField()),
                ('cantidad_cache', models.PositiveIntegerField()),
                ('nucleos', models.PositiveIntegerField()),
                ('hilos', models.PositiveIntegerField()),
                ('cantidad_memoria_mhz', models.PositiveIntegerField(blank=True, null=True)),
                ('adaptador_grafico', models.BooleanField()),
                ('tdp', models.PositiveIntegerField()),
                ('cache_procesador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.CacheProcesador')),
                ('familia_procesador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.FamiliaProcesador')),
                ('litografia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Litografia')),
                ('modelo_procesador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloProcesador')),
                ('so', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.SO')),
                ('socket_procesador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.SocketProcesador')),
                ('tipo_memoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoMemoria')),
            ],
        ),
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('potencia_nominal', models.PositiveIntegerField()),
                ('diametro_ventilador_mm', models.PositiveIntegerField()),
                ('conectores_sata', models.PositiveIntegerField()),
                ('certificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Certificacion')),
                ('factor_forma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.FactorForma')),
                ('modelo_psu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloPSU')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('cantidad_memoria_gb', models.PositiveIntegerField()),
                ('cantidad_memoria_mhz', models.PositiveIntegerField()),
                ('latencia', models.PositiveIntegerField()),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('factor_forma_ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.FactorFormaRAM')),
                ('modelo_ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloRAM')),
                ('tipo_memoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoMemoria')),
            ],
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('capacidad', models.PositiveIntegerField()),
                ('velocidad_escritura', models.PositiveIntegerField()),
                ('velocidad_lectura', models.PositiveIntegerField()),
                ('interfazdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.InterfazDD')),
                ('modelo_dd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloDD')),
                ('tamdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TamDD')),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaMadre',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('cantidad_memoria_gb', models.PositiveIntegerField()),
                ('cantidad_ranuras_memoria', models.PositiveIntegerField()),
                ('cantidad_puertos_pci', models.PositiveIntegerField()),
                ('cantidad_puertos_usb3', models.PositiveIntegerField()),
                ('cantidad_puertos_usb2', models.PositiveIntegerField()),
                ('cantidad_puertos_sata', models.PositiveIntegerField()),
                ('cantidad_puertos_hdmi', models.PositiveIntegerField()),
                ('chipset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Chipset')),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('factor_forma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.FactorForma')),
                ('familia_procesador', models.ManyToManyField(to='caracteristicas.FamiliaProcesador')),
                ('modelo_tarjeta_madre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloTarjetaMadre')),
                ('para_marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Marca')),
                ('socket_procesador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.SocketProcesador')),
                ('tipo_memoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoMemoria')),
            ],
        ),
        migrations.CreateModel(
            name='TarjetaVideo',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('nucleos_cuda', models.PositiveIntegerField()),
                ('frecuencia_mhz', models.PositiveIntegerField()),
                ('frecuencia_turbo_mhz', models.PositiveIntegerField()),
                ('memoria_grafica_gb', models.PositiveIntegerField()),
                ('ancho_datos_bits', models.PositiveIntegerField()),
                ('version_directx', models.FloatField()),
                ('cantidad_dvi', models.PositiveIntegerField()),
                ('cantidad_hdmi', models.PositiveIntegerField()),
                ('cantidad_displayport', models.PositiveIntegerField()),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('familia_grafica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.FamiliaGrafica')),
                ('modelo_grafica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloGrafica')),
                ('procesador_grafico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ProcesadorGrafico')),
                ('tipo_interfaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoInterfaz')),
                ('tipo_memoria_grafica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoMemoriaGrafica')),
            ],
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('rgb', models.BooleanField()),
                ('colores', models.ManyToManyField(to='caracteristicas.Color')),
                ('conectividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Conectividad')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Idioma')),
                ('modelo_teclado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.ModeloTeclado')),
                ('tipo_interfaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.TipoInterfaz')),
            ],
        ),
    ]
