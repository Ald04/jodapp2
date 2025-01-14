# Generated by Django 5.1.1 on 2024-09-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_evento', '0016_remove_mesa__disponibilidad_remove_mesa__left_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='disponibilidad',
            field=models.BooleanField(default=True, verbose_name='Disponibilidad'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='left',
            field=models.PositiveIntegerField(default=0, verbose_name='Posición Left'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='top',
            field=models.PositiveIntegerField(default=0, verbose_name='Posición Top'),
        ),
    ]
