# Generated by Django 5.1.1 on 2024-10-31 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_ventas', '0009_alter_facturacliente__empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacliente',
            name='_numero_factura',
            field=models.CharField(max_length=100, verbose_name='Número de Factura'),
        ),
    ]
