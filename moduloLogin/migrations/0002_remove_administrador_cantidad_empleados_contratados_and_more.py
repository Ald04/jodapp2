# Generated by Django 5.1 on 2024-08-29 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrador',
            name='cantidad_empleados_contratados',
        ),
        migrations.RemoveField(
            model_name='administrador',
            name='cantidad_fiestas_organizadas',
        ),
    ]
