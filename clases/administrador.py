from .empleado import Empleado

class Administrador(Empleado):
    @property
    def cantidad_empleados_contratados(self):
        from .contratacion import Contratacion
        return Contratacion.objects.filter(_administrador=self, _tipo='Contratacion').count()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cantidad_empleados_contratados})"
    

    def save(self, *args, **kwargs):
        if self._user:
            self._user.is_superuser = True
            self._user.save()
        
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'moduloLogin'
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

