# Generated by Django 5.1 on 2024-09-06 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0002_contratacion__tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='_estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Inactivo', max_length=50),
        ),
    ]
