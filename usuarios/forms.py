from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from usuarios.models import BaseUser


class RegistrarForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(
        choices=[("cliente", "Cliente"), ("profissional", "Profissional")],
    )

    class Meta:
        model = BaseUser
        fields = ["username", "password1", "password2", "tipo_usuario"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "ruangustavo"},
        ),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={"class": "input input-bordered w-full", "placeholder": "********"},
        ),
    )
