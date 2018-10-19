# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-09 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadoVenta',
            fields=[
                ('id_estado_venta', models.AutoField(primary_key=True, serialize=False)),
                ('estado_venta', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='producto.Producto')),
                ('porciento_desc', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tipo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('estado_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.EstadoVenta')),
                ('tipo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.TipoPago')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Venta'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto'),
        ),
    ]
