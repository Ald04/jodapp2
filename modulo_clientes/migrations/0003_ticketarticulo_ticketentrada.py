# Generated by Django 5.1.1 on 2024-11-01 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_clientes', '0002_cliente__foto'),
        ('modulo_evento', '0028_delete_cliente'),
        ('modulo_stock', '0009_remitoproveedor__empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('_fecha_limite', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Límite')),
                ('_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_stock.articulo', verbose_name='Bebida')),
                ('_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_clientes.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Ticket Bebida',
                'verbose_name_plural': 'Tickets Bebidas',
            },
        ),
        migrations.CreateModel(
            name='TicketEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_clientes.cliente', verbose_name='Cliente')),
                ('_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_evento.entrada', verbose_name='Entrada')),
            ],
            options={
                'verbose_name': 'Ticket Entrada',
                'verbose_name_plural': 'Tickets Entradas',
            },
        ),
    ]
