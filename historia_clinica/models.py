from django.db import models



class Paciente(models.Model):
    nombre = models.CharField(max_length=80)
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Paciente: {self.nombre}"


class HistoriaClinica(models.Model):

    motivo_consulta = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    observaciones = models.TextField(blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField()

    def __str__(self):
        return f"Historia de {self.paciente.nombre}"