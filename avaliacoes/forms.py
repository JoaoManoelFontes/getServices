from django import forms

from avaliacoes.models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ["nota", "comentario"]
        widgets = {
            "nota": forms.RadioSelect(),
            "comentario": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full",
                },
            ),
        }
