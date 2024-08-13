from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Comentario(models.Model):
    avaliacao = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    texto = models.TextField()
    autor = models.ForeignKey("usuarios.Cliente", on_delete=models.CASCADE)
    alvo = models.ForeignKey("usuarios.Profissional", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.texto
