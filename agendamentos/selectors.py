from django.utils import timezone

from usuarios.models import Profissional

from .models import Agendamento, Horario


def get_profissional_schedule(profissional: Profissional) -> dict:
    """Retorna os horários e agendamentos do profissional a partir da data atual, com limite de 25 itens cada"""
    data_atual = timezone.now()

    horarios = Horario.objects.filter(
        profissional=profissional, data_inicio__gte=data_atual
    ).order_by("data_inicio")[:25]

    agendamentos = Agendamento.objects.filter(
        profissional=profissional, horario__data_inicio__gte=data_atual
    ).select_related("horario")[:25]

    return {
        "horarios": horarios,
        "agendamentos": agendamentos,
    }
