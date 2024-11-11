# Generated by Django 5.1.1 on 2024-09-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_evento', '0014_fiesta__publicada_alter_mesa__capacidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='_left',
            field=models.PositiveIntegerField(default=0, verbose_name='Posición Left'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='_top',
            field=models.PositiveIntegerField(default=0, verbose_name='Posición Top'),
        ),
    ]
