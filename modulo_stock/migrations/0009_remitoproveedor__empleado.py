# Generated by Django 5.1.1 on 2024-10-06 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0015_alter_empleado__annos_experiencia'),
        ('modulo_stock', '0008_alter_movimientostock__cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='remitoproveedor',
            name='_empleado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='moduloLogin.empleado', verbose_name='Empleado'),
        ),
    ]