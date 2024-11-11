from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.contrib.auth.models import User

class Facultad(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class Departamento(models.Model):	
	nombre = models.CharField(max_length=100)
	facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
	director = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

class Carrera(models.Model):
	nombre = models.CharField(max_length=100)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	pensum = models.ForeignKey('Pensum', on_delete=models.SET_NULL, blank=True, null=True, related_name='pensums_de_carrera') 
	def __str__(self):
		return self.nombre

class Pensum(models.Model):
	nombre = models.CharField(max_length=100)
	carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carreras_de_pensum',null=True, blank=True)
	semestres = models.ManyToManyField('Semestre')
	def __str__(self):
		return self.nombre

class Semestre(models.Model):
	nombre = models.CharField(max_length=100)
	materias = models.ForeignKey('Materia', related_name='semestres',  on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.nombre

class Materia(models.Model):
	nombre = models.CharField(max_length=100)
	codigo = models.CharField(max_length=20)
	creditos = models.IntegerField()
	semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, null=True, blank=True)
	hasEquivalency = models.BooleanField(default=False)
	equivalencia = models.ManyToManyField('Materia', blank=True) 
	cupos = models.IntegerField()
	horario = models.ManyToManyField('Horario')
	profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

class Asistencia(models.Model):
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	horario =  models.DateField()
	estudiantes = models.ManyToManyField('Estudiante')
	def __str__(self):
		return self.materia.nombre

class Chat(models.Model):
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	participantes = models.ManyToManyField('Estudiante')
	moderador = models.ForeignKey('Profesor', on_delete=models.CASCADE)
	mensajes = models.CharField(max_length=100)
	def __str__(self):
		return self.materia.nombre

class Horario(models.Model):
	dia = models.CharField(max_length=10)
	horaInicio = models.CharField(max_length=7)
	horaFin = models.CharField(max_length=7)
	def __str__(self):
		return self.dia + self.horaInicio + self.horaFin

class Persona(models.Model):
	nombreCompleto = models.CharField(max_length=100)
	fechaNacimiento = models.DateField()
	codigo = models.CharField(max_length=15)
	documento = models.CharField(max_length=20)
	celular = models.CharField(max_length=10)
	correoPersonal = models.CharField(max_length=100, unique=True)
	correoInstitucional = models.CharField(max_length=100, unique=True)
	direccion = models.CharField(max_length=100)
	grupoSanguineo = models.CharField(max_length=3)
	def __str__(self):
		return self.nombreCompleto

class Profesor(Persona):
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	tipoVinculacion = models.CharField(max_length=20)
	especialidad = models.CharField(max_length=50)
	def __str__(self):
		return self.nombreCompleto

class Estudiante(Persona):
	estadoAcademico = models.CharField(max_length=20)
	numeroMatricula = models.CharField(max_length=20)
	fechaInscripcion = models.DateField()
	carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default="1")
	pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE, default="1")
	def __str__(self):
		return self.nombreCompleto
    
class MatriculaMateria(models.Model):
	periodoAcademico = models.ForeignKey('periodoAcademico', on_delete=models.CASCADE)
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	def __str__(self):
		return self.estudiante.nombreCompleto + self.materia.nombre
	#Definir la matricula de una materia de un estudiante

class PeriodoAcademico(models.Model):
	periodoAcademico = models.CharField(max_length=100)
	def __str__(self):
		return self.periodoAcademico
	
class NotaMateria(models.Model):
	periodoAcademico = models.CharField(max_length=100)
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
	primerPrevio = models.FloatField()
	segundoPrevio = models.FloatField() 
	tercerPrevio = models.FloatField()
	examenFinal = models.FloatField()
	def __str__(self):
		return self.materia.nombre

class HistoricoNotas(models.Model):
    periodoAcademico = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materias = models.ManyToManyField(Materia)

class UsuarioCarnet(models.Model):
	persona = models.OneToOneField(Persona, related_name='usuario_carnet_persona', on_delete=models.CASCADE)
	carrera = models.OneToOneField(Carrera, on_delete=models.CASCADE)

	def __str__(self):
		 return self.persona.nombreCompleto + self.carrera.nombre
	

class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('if_staff', False)     
		extra_fields.setdefault('if_superuser', False)

		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')

		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('if_staff', True)
		extra_fields.setdefault('if_superuser', True)

		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.save()

		return user
     
class AppUser(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	username = models.CharField(max_length=50)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='persona_user')
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [ 'persona']
	
	objects = AppUserManager()

	def __str__(self):
		return self.username
    