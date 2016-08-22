from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    Nombre =  models.CharField(max_length=30, null=False, blank=False)
    Apellido = models.CharField(max_length=50, null=False, blank=False)
    DNI = models.IntegerField(null=False, blank=False)
    Telefono = models.IntegerField()

    def __str__(self):
        return str(self.DNI)

class Doctor (models.Model):
    Nombre =  models.CharField(max_length=30, null=False, blank=False)
    Apellido = models.CharField(max_length=50, null=False, blank=False)
    DNI = models.IntegerField(null=False, blank=False)
    Telefono = models.IntegerField()
    Especialidad = models.ForeignKey('Especialidad')
    Correo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Especialidad)+' '+ self.Nombre

class Turno(models.Model):
    Fecha= models.DateField()
    Hora= models.TimeField()
    Doctor= models.ForeignKey ('Doctor')
    Paciente = models.ForeignKey('Paciente')

    def __str__(self):
        return str(self.Paciente)+' '+ str(self.Fecha) +' '+ str(self.Hora)

class Especialidad (models.Model):
    Nombre = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.Nombre