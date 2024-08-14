from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from agendamentos.models import Horario


class HorarioForm(forms.ModelForm):
    data = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(
            attrs={"type": "datetime-local"},
        ),
    )

    class Meta:
        model = Horario
        fields = ("data", "vago")

    def clean(self) -> dict[str, Any]:
        data = self.cleaned_data.get("data")
        now = datetime.now(tz=timezone.utc)

        if data <= now:
            raise ValidationError("Data inválida!")
        return super().clean()
