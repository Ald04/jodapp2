# Generated by Django 5.1 on 2024-09-10 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleremitoproveedor',
            old_name='_id_producto',
            new_name='_producto',
        ),
        migrations.RenameField(
            model_name='detalleremitoproveedor',
            old_name='_id_remito',
            new_name='_remito',
        ),
        migrations.RenameField(
            model_name='fabricacion',
            old_name='_id_producto',
            new_name='_producto',
        ),
        migrations.RenameField(
            model_name='fabricacion',
            old_name='_id_trago',
            new_name='_trago',
        ),
        migrations.RenameField(
            model_name='movimientostock',
            old_name='_id_empleado',
            new_name='_empleado',
        ),
        migrations.RenameField(
            model_name='movimientostock',
            old_name='_id_producto',
            new_name='_producto',
        ),
        migrations.RenameField(
            model_name='remitoproveedor',
            old_name='_id_proveedor',
            new_name='_proveedor',
        ),
    ]
