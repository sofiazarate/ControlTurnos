from django.contrib import admin
from .models import Paciente
from .models import Doctor
from .models import Turno
from .models import Especialidad

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Turno)
admin.site.register(Especialidad)