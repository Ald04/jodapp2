# Generated by Django 5.1 on 2024-09-11 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0007_alter_auditor__frecuencia_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrador',
            options={'verbose_name': 'Administrador', 'verbose_name_plural': 'Administradores'},
        ),
        migrations.AlterModelOptions(
            name='auditor',
            options={'verbose_name': 'Auditor', 'verbose_name_plural': 'Auditores'},
        ),
        migrations.AlterModelOptions(
            name='bartender',
            options={'verbose_name': 'Bartender', 'verbose_name_plural': 'Bartenders'},
        ),
        migrations.AlterModelOptions(
            name='cajero',
            options={'verbose_name': 'Cajero', 'verbose_name_plural': 'Cajeros'},
        ),
        migrations.AlterModelOptions(
            name='contratacion',
            options={'verbose_name': 'Contratación', 'verbose_name_plural': 'Gestión de contrataciones'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado'},
        ),
        migrations.AlterModelOptions(
            name='mozo',
            options={'verbose_name': 'Mozo', 'verbose_name_plural': 'Mozos'},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='seguridad',
            options={'verbose_name': 'Guardia de Seguridad', 'verbose_name_plural': 'Guardias de Seguridad'},
        ),
        migrations.AlterModelOptions(
            name='supervisor',
            options={'verbose_name': 'Supervisor', 'verbose_name_plural': 'Supervisores'},
        ),
        migrations.AlterModelOptions(
            name='turno',
            options={'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
    ]
