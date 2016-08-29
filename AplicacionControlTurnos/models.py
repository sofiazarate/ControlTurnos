from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    Nombre =  models.CharField(max_length=30, blank=False)
    Apellido = models.CharField(max_length=50, blank=False)
    DNI = models.IntegerField(null=False, blank=False)
    Telefono = models.IntegerField()

    def __str__(self):
        return str(self.DNI)

class Doctor (models.Model):
    Nombre =  models.CharField(max_length=30,blank=False)
    Apellido = models.CharField(max_length=50, blank=False)
    DNI = models.IntegerField(null=False, blank=False)
    Telefono = models.IntegerField()
    Especialidad = models.ForeignKey('Especialidad')
    Correo = models.CharField(max_length=50)
    HorariosLaborales = models.ForeignKey('HorariosLaborales')
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
    Nombre = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.Nombre

class HorariosLaborales (models.Model):
    lunes=1
    martes=2
    miercoles=3
    jueves=4
    viernes=5
    sabado=6
    domingo=0

    opcionesDias=(
        (lunes,'Lunes'),
        (martes,'Martes'),
        (miercoles,'Miercoles'),
        (jueves,'Jueves'),
        (viernes,'Viernes'),
        (sabado,'Sabado'),
        (domingo,'Domingo')
        )
    Dia=models.IntegerField(choices=opcionesDias,default=domingo)
    HoraInicio= models.TimeField()
    HoraFin= models.TimeField()

    def __str__(self):
        return str(self.Dia)+' '+ str(self.HoraInicio) +' '+ str(self.HoraFin)