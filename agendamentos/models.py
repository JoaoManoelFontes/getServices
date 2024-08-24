from datetime import datetime, timedelta

from dateutil.rrule import DAILY, MONTHLY, WEEKLY, rrule
from django.db import models
from django.utils import timezone


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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.profissional.servico.nome} - {self.cliente}"


class Horario(models.Model):
    profissional = models.ForeignKey(
        "usuarios.Profissional",
        on_delete=models.CASCADE,
    )
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    vago = models.BooleanField(default=True)

    FREQUENCIA_CHOICES = [
        ("UNICA", "Não se repete"),
        ("DIARIA", "Todos os dias"),
        ("SEMANAL", "Semanalmente"),
        ("MENSAL", "Mensalmente"),
    ]
    frequencia = models.CharField(
        max_length=10,
        choices=FREQUENCIA_CHOICES,
        default="UNICA",
    )

    dias_semana = models.CharField(max_length=13, blank=True, null=True)
    data_fim_recorrencia = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.data_inicio}'

    def gerar_horarios_recorrentes(self):
        if self.frequencia == "UNICA":
            return [self]

        duracao = self.data_fim - self.data_inicio

        proximo_ano = (self.data_inicio + timedelta(days=365)).date()

        data_fim_recorrencia = self.data_fim_recorrencia or proximo_ano

        if self.data_inicio.tzinfo is None:
            self.data_inicio = timezone.make_aware(self.data_inicio)

        if self.data_fim.tzinfo is None:
            self.data_fim = timezone.make_aware(self.data_fim)

        data_fim_recorrencia = timezone.make_aware(
            datetime.combine(data_fim_recorrencia, self.data_inicio.time()),
        )

        if self.frequencia == "DIARIA":
            datas = list(
                rrule(DAILY, dtstart=self.data_inicio, until=data_fim_recorrencia),
            )
        elif self.frequencia == "SEMANAL":
            dias_semana = (
                [int(dia) for dia in self.dias_semana.split(",")]
                if self.dias_semana
                else None
            )
            datas = list(
                rrule(
                    WEEKLY,
                    dtstart=self.data_inicio,
                    until=data_fim_recorrencia,
                    byweekday=dias_semana,
                ),
            )
        elif self.frequencia == "MENSAL":
            datas = list(
                rrule(MONTHLY, dtstart=self.data_inicio, until=data_fim_recorrencia),
            )
        else:
            return []

        horarios_recorrentes = [
            Horario(
                profissional=self.profissional,
                data_inicio=data,
                data_fim=data + duracao,
                vago=True,
                frequencia="UNICA",
            )
            for data in datas[1:]
        ]

        return horarios_recorrentes
