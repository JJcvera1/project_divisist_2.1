from django.urls import path, include
from rest_framework import routers
from divisist import views

from django.contrib.auth import views as auth_views #RECUPERAR CONTRASEÑA

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

    #llamados del front
    path('login', views.login, name='login'), 
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='user'),  
    path('info-persona', views.view_info, name='info'),
    path('update-info', views.update_user, name='user-update'),  


    #recuperar contraseña
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),   
]