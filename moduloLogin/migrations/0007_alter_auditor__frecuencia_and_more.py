# Generated by Django 5.1 on 2024-09-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0006_remove_persona__domicilio_remove_persona__telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditor',
            name='_frecuencia',
            field=models.PositiveIntegerField(help_text='(días)'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='_frecuencia',
            field=models.PositiveIntegerField(help_text='(días)'),
        ),
    ]
