from __future__ import annotations

from typing import ClassVar

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import BaseUser, Cliente


class BaseUserForm(UserCreationForm):
    model = BaseUser
    fields: ClassVar[list[str]] = ["username", "email", "password1", "password2"]


class ClienteForm(BaseUserForm):
    model = Cliente
    fields: ClassVar[list[str]] = ["user"]

    def __init__(self, *args: list, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()
