from django import forms

from agendamentos.models import Horario


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ("data", "vago")
