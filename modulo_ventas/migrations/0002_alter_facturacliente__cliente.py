# Generated by Django 5.1.1 on 2024-10-09 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_evento', '0027_cliente'),
        ('modulo_ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacliente',
            name='_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulo_evento.cliente', verbose_name='Cliente'),
        ),
    ]
