# Generated by Django 5.1.1 on 2024-10-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='_foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_clientes/'),
        ),
    ]
