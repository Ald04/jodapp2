# Generated by Django 5.1 on 2024-09-10 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_stock', '0002_rename__id_producto_detalleremitoproveedor__producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleremitoproveedor',
            name='_estado_producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulo_stock.estadoproducto'),
        ),
    ]
