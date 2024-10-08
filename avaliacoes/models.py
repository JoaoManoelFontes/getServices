from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Avaliacao(models.Model):
    nota = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comentario = models.TextField()
    cliente = models.ForeignKey("usuarios.Cliente", on_delete=models.CASCADE)
    profissional = models.ForeignKey("usuarios.Profissional", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    agendamento = models.OneToOneField(
        "agendamentos.Agendamento", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.comentario
