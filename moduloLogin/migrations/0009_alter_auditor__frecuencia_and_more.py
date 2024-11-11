# Generated by Django 5.1 on 2024-09-12 15:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloLogin', '0008_alter_administrador_options_alter_auditor_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditor',
            name='_frecuencia',
            field=models.PositiveIntegerField(help_text='(días)', verbose_name='Frecuencia'),
        ),
        migrations.AlterField(
            model_name='bartender',
            name='_barra_asignada',
            field=models.CharField(max_length=100, verbose_name='Barra Asignada'),
        ),
        migrations.AlterField(
            model_name='cajero',
            name='_caja_asignada',
            field=models.CharField(max_length=100, verbose_name='Caja Asignada'),
        ),
        migrations.AlterField(
            model_name='contratacion',
            name='_administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contrataciones_administradas', to='moduloLogin.administrador', verbose_name='Administrador'),
        ),
        migrations.AlterField(
            model_name='contratacion',
            name='_empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contrataciones', to='moduloLogin.empleado', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='contratacion',
            name='_fecha_contratacion',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Contratación'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='_annos_experiencia',
            field=models.PositiveIntegerField(verbose_name='Años de experiencia'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='_estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Inactivo', max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='_fecha_inicio',
            field=models.DateField(verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='_seniority',
            field=models.CharField(choices=[('Trainee', 'Trainee'), ('Junior', 'Junior'), ('Senior', 'Senior')], max_length=50, verbose_name='Seniority'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='_sueldo',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sueldo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='_zona_asignada',
            field=models.CharField(choices=[('Planta baja', 'Planta baja'), ('Primer piso', 'Primer piso')], max_length=100, verbose_name='Zona Asignada'),
        ),
        migrations.AlterField(
            model_name='empleadotieneturno',
            name='_empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloLogin.empleado', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='empleadotieneturno',
            name='_turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloLogin.turno', verbose_name='Turno'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='_apellido',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='_cuil',
            field=models.CharField(max_length=20, unique=True, verbose_name='CUIL'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='_dni',
            field=models.CharField(max_length=20, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='_fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='_nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='seguridad',
            name='_entrada_asignada',
            field=models.CharField(max_length=100, verbose_name='Entrada Asignada'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='_frecuencia',
            field=models.PositiveIntegerField(help_text='(días)', verbose_name='Frecuencia'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='_hora_fin',
            field=models.TimeField(verbose_name='Hora Fin'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='_hora_inicio',
            field=models.TimeField(verbose_name='Hora Inicio'),
        ),
    ]
