# Generated by Django 5.1.1 on 2024-09-19 22:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_evento', '0011_alter_evento__descripcion_alter_evento__edad_maxima_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='_fecha',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
    ]
