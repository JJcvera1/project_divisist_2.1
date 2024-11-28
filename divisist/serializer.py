from django.forms import ValidationError
from rest_framework import serializers
from .models import (Facultad, Departamento, Semestre, Pensum, Carrera, Horario, Persona, Profesor, Estudiante, Materia, Asistencia, Chat, MatriculaMateria, 
                    NotaMateria, HistoricoNotas, UsuarioCarnet, AppUser)
from django.contrib.auth import get_user_model, authenticate

import logging
logger = logging.getLogger(__name__)

UserModel = get_user_model()

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facultad
        fields= '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departamento
        fields='__all__'     

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Semestre
        fields='__all__'

class PensumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pensum
        fields='__all__'

class CarreraSerializar(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields='__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Horario
        fields='__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields='__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields='__all__'

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materia
        fields='__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Asistencia
        fields='__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'

class MatriculaMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=MatriculaMateria
        fields='__all__'

class NotaMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotaMateria
        fields='__all__'

class HistoricoNotasSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistoricoNotas
        fields='__all__'

class UsuarioCarnetSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioCarnet
        fields='__all__'

class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUser
        fields='__all__'

#class UserLoginSerializer(serializers.Serializer):
#    email = serializers.EmailField()
#    password = serializers.CharField()
#	##
#    logger.info({email})
#    logger.info({password})
#    def check_user(self, clean_data):
#        user = authenticate(username=clean_data['email'], password=clean_data['password'])
#        if not user:
#            logger.error("Validación fallida. Usuario o contraseña incorrectos.")
#            raise ValidationError('user not found')
#        return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('email', 'username')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields = ['celular', 'correoPersonal', 'direccion']