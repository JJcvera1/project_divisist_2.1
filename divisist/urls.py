from django.urls import path, include
from rest_framework import routers
from divisist import views

app_name = "divisist"
router = routers.DefaultRouter()
router.register(r'facultad', views.FacultadViewSet)
router.register(r'departamento', views.DepartamentoViewSet)
router.register(r'semestre', views.SemestreViewSet)
router.register(r'pensum', views.PensumViewSet)
router.register(r'carrera', views.CarreraViewSet)
router.register(r'horario', views.HorarioViewSet)
router.register(r'persona', views.PersonaViewSet)
router.register(r'profesor', views.ProfesorViewSet)
router.register(r'estudiante', views.EstudianteViewSet)
router.register(r'materia', views.MateriaViewSet)
router.register(r'asistencia', views.AsistenciaViewSet)
router.register(r'chat', views.ChatViewSet)
router.register(r'matricula_materia', views.MatriculaMateriaViewSet)
router.register(r'nota_materia', views.NotaMateriaViewSet)
router.register(r'historico_notas', views.HistoricoNotasViewSet)
router.register(r'usuario_carnet', views.UsuarioCarnetViewSet)
router.register(r'app_user', views.UserAppViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.UserLogin.as_view(), name='login'), 
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),  
]