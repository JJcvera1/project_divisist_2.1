from django.contrib import admin
from .models import (Facultad, Departamento, Semestre, Pensum, Carrera, Horario, Persona, Profesor, Estudiante, Materia, Asistencia, Chat, MatriculaMateria, 
                    NotaMateria, HistoricoNotas, UsuarioCarnet, AppUser)

# Register your models here.

admin.site.register(Facultad)
admin.site.register(Departamento) 
admin.site.register(Semestre)
admin.site.register(Pensum)
admin.site.register(Carrera)
admin.site.register(Horario)
admin.site.register(Persona)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Asistencia)
admin.site.register(Chat)
admin.site.register(MatriculaMateria)
admin.site.register(NotaMateria)
admin.site.register(HistoricoNotas)
admin.site.register(UsuarioCarnet)
admin.site.register(AppUser)