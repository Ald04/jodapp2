# Generated by Django 5.1 on 2024-09-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_evento', '0009_rename__latitud_evento_latitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='latitud',
            field=models.DecimalField(decimal_places=10, default=-26.1855, max_digits=12),
        ),
        migrations.AlterField(
            model_name='evento',
            name='longitud',
            field=models.DecimalField(decimal_places=10, default=-58.1739, max_digits=12),
        ),
    ]
