from django import forms

from agendamentos.models import Horario


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ["data_inicio", "data_fim", "frequencia", "data_fim_recorrencia"]
        widgets = {
            "data_inicio": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "input input-bordered w-full"},
            ),
            "data_fim": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "input input-bordered w-full"},
            ),
            "data_fim_recorrencia": forms.DateInput(
                attrs={"type": "date", "class": "input input-bordered w-full"},
            ),
            "frequencia": forms.Select(
                attrs={"class": "select select-bordered w-full"},
            ),
        }
        labels = {
            "data_inicio": "Data inicial",
            "data_fim": "Data final",
            "frequencia": "Repetir",
            "data_fim_recorrencia": "Repetir até",
        }

    DIAS_SEMANA_CHOICES = [
        ("0", "Segunda-feira"),
        ("1", "Terça-feira"),
        ("2", "Quarta-feira"),
        ("3", "Quinta-feira"),
        ("4", "Sexta-feira"),
        ("5", "Sábado"),
        ("6", "Domingo"),
    ]
    dias_semana = forms.MultipleChoiceField(
        choices=DIAS_SEMANA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Dias da semana",
    )

    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.dias_semana:
            self.initial["dias_semana"] = self.instance.dias_semana.split(",")

    def clean(self):
        cleaned_data = super().clean()
        frequencia = cleaned_data.get("frequencia")
        dias_semana = cleaned_data.get("dias_semana")

        if frequencia == "SEMANAL" and not dias_semana:
            raise forms.ValidationError(
                "Por favor, selecione os dias da semana para a frequência semanal.",
            )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        dias_semana = self.cleaned_data.get("dias_semana")

        if dias_semana:
            instance.dias_semana = ",".join(dias_semana)

        if commit:
            instance.save()

        return instance
