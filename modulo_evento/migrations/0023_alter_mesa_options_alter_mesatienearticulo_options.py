# Generated by Django 5.1.1 on 2024-09-26 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_evento', '0022_mesatienearticulo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mesa',
            options={'ordering': ['_fiesta___fecha', '_fiesta___nombre'], 'verbose_name': 'Gestión de Mesas', 'verbose_name_plural': 'Gestión de Mesas'},
        ),
        migrations.AlterModelOptions(
            name='mesatienearticulo',
            options={'verbose_name': 'Gestión de Bebidas', 'verbose_name_plural': 'Gestión de Bebidas'},
        ),
    ]