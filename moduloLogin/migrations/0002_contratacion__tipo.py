# Generated by Django 5.1 on 2024-09-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratacion',
            name='_tipo',
            field=models.CharField(choices=[('Contratacion', 'Contratacion'), ('Renovacion', 'Renovacion'), ('Despido', 'Despido')], default='Contratacion', max_length=50),
            preserve_default=False,
        ),
    ]
