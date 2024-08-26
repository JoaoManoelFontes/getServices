from datetime import timedelta

from dateutil.relativedelta import relativedelta
from django.test import TestCase
from django.utils import timezone

from servicos.models import Servico
from usuarios.models import BaseUser, Profissional

from .models import Horario


class HorarioModelTest(TestCase):
    def setUp(self):
        self.user = BaseUser.objects.create_user(username="testuser", password="12345")
        servico = Servico.objects.create(
            nome="Serviços gerais",
            descricao="Serviços gerais",
        )
        self.profissional = Profissional.objects.create(user=self.user, servico=servico)
        self.horario = Horario.objects.create(
            profissional=self.profissional,
            data_inicio=timezone.now(),
            data_fim=timezone.now() + timedelta(hours=1),
            frequencia="UNICA",
        )

    def test_horario_creation(self):
        self.assertTrue(isinstance(self.horario, Horario))
        self.assertEqual(
            self.horario.__str__(),
            f"{self.profissional.user} - {self.horario.data_inicio}",
        )

    def test_gerar_horarios_recorrentes_unica(self):
        horarios = self.horario.gerar_horarios_recorrentes()
        self.assertEqual(len(horarios), 1)
        self.assertEqual(horarios[0], self.horario)

    def test_gerar_horarios_recorrentes_diaria(self):
        self.horario.frequencia = "DIARIA"
        self.horario.data_fim_recorrencia = timezone.now().date() + timedelta(days=5)
        self.horario.save()
        horarios = self.horario.gerar_horarios_recorrentes()
        self.assertEqual(len(horarios), 5)

    def test_gerar_horarios_recorrentes_semanal(self):
        self.horario.frequencia = "SEMANAL"
        self.horario.dias_semana = "0,2,4"
        self.horario.data_fim_recorrencia = timezone.now().date() + timedelta(days=14)
        self.horario.save()
        horarios = self.horario.gerar_horarios_recorrentes()
        self.assertGreater(len(horarios), 0)

    def test_gerar_horarios_recorrentes_mensal(self):
        now = timezone.now()
        self.horario.frequencia = "MENSAL"
        self.horario.data_inicio = now
        self.horario.data_fim = now + timedelta(hours=1)
        self.horario.data_fim_recorrencia = now.date() + relativedelta(months=2)
        self.horario.save()

        horarios = self.horario.gerar_horarios_recorrentes()

        self.assertEqual(len(horarios), 2)

        expected_dates = [now + relativedelta(months=1), now + relativedelta(months=2)]

        for horario, expected_date in zip(horarios, expected_dates):
            self.assertEqual(horario.data_inicio.date(), expected_date.date())
