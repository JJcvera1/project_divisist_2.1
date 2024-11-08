from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class Facultad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    director = models.CharField(max_length=100)

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    pensum = models.ForeignKey('Pensum', on_delete=models.SET_NULL, blank=True, null=True, related_name='pensums_de_carrera') 

class Pensum(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carreras_de_pensum',null=True, blank=True)
    semestres = models.ManyToManyField('Semestre')

class Semestre(models.Model):
    nombre = models.CharField(max_length=100)
    materias = models.ForeignKey('Materia', related_name='semestres',  on_delete=models.CASCADE, null=True, blank=True)

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    creditos = models.IntegerField()
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, null=True, blank=True)
    hasEquivalency = models.BooleanField(default=False)
    equivalencia = models.ManyToManyField('Materia') 
    cupos = models.IntegerField()
    horario = models.ManyToManyField('Horario')
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)

class Asistencia(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    horario =  models.DateField()
    estudiantes = models.ManyToManyField('Estudiante')

class Chat(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    participantes = models.ManyToManyField('Estudiante')
    moderador = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    mensajes = models.CharField(max_length=100)

class Horario(models.Model):
    dia = models.CharField(max_length=10)
    horaInicio = models.CharField(max_length=7)
    horaFin = models.CharField(max_length=7)

class Persona(models.Model):
    nombreCompleto = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    codigo = models.CharField(max_length=15)
    celular = models.CharField(max_length=10)
    correoPersonal = models.CharField(max_length=100, unique=True)
    correoInstitucional = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    grupoSanguineo = models.CharField(max_length=3)

class Profesor(Persona):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    tipoVinculacion = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50)

class Estudiante(Persona):
    estadoAcademico = models.CharField(max_length=20)
    numeroMatricula = models.CharField(max_length=20)
    fechaInscripcion = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default="1")
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE, default="1")
    
class MatriculaMateria(models.Model):
    periodoAcademico = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    #Definir la matricula de una materia de un estudiante
class NotaMateria(models.Model):
    periodoAcademico = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    primerPrevio = models.FloatField()
    segundoPrevio = models.FloatField() 
    tercerPrevio = models.FloatField()
    examenFinal = models.FloatField()

class HistoricoNotas(models.Model):
    periodoAcademico = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materias = models.ManyToManyField(Materia)

class UsuarioCarnet(models.Model):
    nombreCompleto = models.OneToOneField(Persona, related_name='usuario_carnet_nombre', on_delete=models.CASCADE)
    codigo = models.OneToOneField(Persona, on_delete=models.CASCADE)
    documento = models.OneToOneField(Persona, related_name='usuario_carnet_documento',  on_delete=models.CASCADE)
    carrera = models.OneToOneField(Carrera, on_delete=models.CASCADE)
    grupoSanguineo = models.OneToOneField(Persona, related_name='usuario_carnet_grupo',  on_delete=models.CASCADE)
