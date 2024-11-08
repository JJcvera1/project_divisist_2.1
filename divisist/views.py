from rest_framework import viewsets
from .serializer import AsistenciaSerializer, CarreraSerializar, ChatSerializer, EstudianteSerializer, FacultadSerializer, DepartamentoSerializer, HistoricoNotasSerializer, HorarioSerializer, MateriaSerializer, MatriculaMateriaSerializer, NotaMateriaSerializer, PensumSerializer, PersonaSerializer, ProfesorSerializer, SemestreSerializer, UsuarioCarnetSerializer, UserLoginSerializer, UserSerializer
from .models import Facultad, Departamento, Semestre, Pensum, Carrera, Horario, Persona, Profesor, Estudiante, Materia, Asistencia, Chat, MatriculaMateria, NotaMateria, HistoricoNotas, UsuarioCarnet
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password


# Create your views here.

class FacultadViewSet(viewsets.ModelViewSet):
    queryset=Facultad.objects.all()
    serializer_class=FacultadSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset=Departamento.objects.all() 
    serializer_class=DepartamentoSerializer 

class SemestreViewSet(viewsets.ModelViewSet):
    queryset=Semestre.objects.all()
    serializer_class=SemestreSerializer

class PensumViewSet(viewsets.ModelViewSet):
    queryset=Pensum.objects.all()
    serializer_class=PensumSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset=Carrera.objects.all()
    serializer_class=CarreraSerializar

class HorarioViewSet(viewsets.ModelViewSet):
    queryset=Horario.objects.all()
    serializer_class=HorarioSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class=PersonaSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset=Profesor.objects.all()
    serializer_class=ProfesorSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class=EstudianteSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset=Materia.objects.all()
    serializer_class=MateriaSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset=Asistencia.objects.all()
    serializer_class=AsistenciaSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset=Chat.objects.all()
    serializer_class=ChatSerializer

class MatriculaMateriaViewSet(viewsets.ModelViewSet):
    queryset=MatriculaMateria.objects.all()
    serializer_class=MatriculaMateriaSerializer

class NotaMateriaViewSet(viewsets.ModelViewSet):
    queryset=NotaMateria.objects.all()
    serializer_class=NotaMateriaSerializer

class HistoricoNotasViewSet(viewsets.ModelViewSet):
    queryset=HistoricoNotas.objects.all()
    serializer_class=HistoricoNotasSerializer

class UsuarioCarnetViewSet(viewsets.ModelViewSet):
    queryset=UsuarioCarnet.objects.all()
    serializer_class=UsuarioCarnetSerializer

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny)
    authentication_classes = (SessionAuthentication, )

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)