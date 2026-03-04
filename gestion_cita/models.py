from django.db import models

class Cita(models.Model):

    paciente = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(null=False, blank=False)
    motivo = models.TextField(help_text="Escriba el motivo de la cita")
    estado = models.CharField(max_length=50)

    def _str_(self):
        return f"Paciente: {self.paciente}"

class CrearCita(models.Model):

    tipo_cita = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)
    agenda = models.DateTimeField()
    estado = models.CharField(max_length=20, default="Pendiente")

    def _str_(self):
        return f"Paciente: {self.tipo_cita}"