from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import AppUser

class CustomUserCreationForm(forms.ModelForm):
    """Formulario para crear nuevos usuarios con una contraseña."""

    class Meta:
        model = AppUser
        fields = ['email']

    def clean_password(self):
        # Verifica que las contraseñas coincidan
        password = self.cleaned_data.get("password")
        return password2

    def save(self, commit=True):
        # Guarda la contraseña encriptada
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    """Formulario para actualizar usuarios, incluye la contraseña como campo de solo lectura."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = AppUser
        fields = ['email', 'password', 'is_active', 'is_staff']
