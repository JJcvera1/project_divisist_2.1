from rest_framework import viewsets
from .serializer import (AsistenciaSerializer, CarreraSerializar, ChatSerializer, EstudianteSerializer, FacultadSerializer, DepartamentoSerializer, 
                        HistoricoNotasSerializer, HorarioSerializer, MateriaSerializer, MatriculaMateriaSerializer, NotaMateriaSerializer, PensumSerializer,  
                        PersonaSerializer, ProfesorSerializer, SemestreSerializer, UsuarioCarnetSerializer, #UserLoginSerializer, 
                        UserAppSerializer, UserUpdateSerializer)
from .models import (Facultad, Departamento, Semestre, Pensum, Carrera, Horario, Persona, Profesor, Estudiante, Materia, Asistencia, Chat, MatriculaMateria, 
                    NotaMateria, HistoricoNotas, UsuarioCarnet, AppUser)
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView

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

class UserAppViewSet(viewsets.ModelViewSet):
    queryset=AppUser.objects.all()
    serializer_class=UserAppSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    print(request.data)
    user = get_object_or_404(AppUser, email=request.data['email'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserAppSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.user)
    return Response("You are login with {}".format(request.user.username), status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_info(request):
    estudiante = Estudiante.objects.get(id=request.data['id'])
    print(estudiante)
    serializer = EstudianteSerializer(instance=estudiante)
    print(request.data)
    print(serializer)
    return Response({"persona": serializer.data}, status=status.HTTP_200_OK)


#recuperar contraseña

from django.utils.decorators import method_decorator
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url
from django.contrib.auth import update_session_auth_hash

UserModel = get_user_model()
class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"title": self.title, "subtitle": None, **(self.extra_context or {})}
        )
        return context
class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("userauths:password_reset_done")
    template_name = "registration/password_reset_form.html"
    title = _("Password reset")
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)

INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_done.html"
    title = _("Password reset sent")


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = reverse_lazy("userauths:password_reset_complete")
    template_name = "registration/password_reset_confirm.html"
    title = _("Enter new password")
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": _("Password reset unsuccessful"),
                    "validlink": False,
                }
            )
        return context


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_reset_complete.html"
    title = _("Password reset complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "registration/password_change_form.html"
    title = _("Password change")

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_change_done.html"
    title = _("Password change successful")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    estudiante = Estudiante.objects.get(id=request.data['id'])
    serializer = UserUpdateSerializer(estudiante, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)