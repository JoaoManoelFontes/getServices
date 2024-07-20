from django.db import models


class Agendamento(models.Model):
    profissional = models.ForeignKey(
        "usuarios.Profissional",
        on_delete=models.CASCADE,
    )
    cliente = models.ForeignKey(
        "usuarios.Cliente",
        on_delete=models.CASCADE,
    )
    horario = models.ForeignKey("Horario", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.profissional.servico.nome} - {self.cliente.username}"


class Horario(models.Model):
    profissional = (
        models.ForeignKey(
            "usuarios.Profissional",
            on_delete=models.CASCADE,
        ),
    )
    data = models.DateTimeField()
    vago = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.profissional.nome} - {self.data}"
