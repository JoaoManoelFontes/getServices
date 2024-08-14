from django import forms

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
