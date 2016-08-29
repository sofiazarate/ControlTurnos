from django.contrib import admin
from .models import Paciente
from .models import Doctor
from .models import Turno
from .models import Especialidad
from .models import HorariosLaborales

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Turno)
admin.site.register(Especialidad)
admin.site.register(HorariosLaborales)