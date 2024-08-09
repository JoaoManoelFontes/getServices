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
    status_choices = (
        ("Pendente", "Pendente"),
        ("Concluido", "Concluido"),
        ("Cancelado", "Cancelado"),
    )
    status = models.CharField(
        max_length=9,
        choices=status_choices,
        default="Pendente",
    )

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
