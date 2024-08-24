from django.utils import timezone

from usuarios.models import Profissional

from .models import Horario


def get_horarios(profissional: Profissional) -> list:
    """Retorna os horários do profissional a partir da data atual, com limite de 25 itens"""
    data_atual = timezone.now()

    return Horario.objects.filter(
        profissional=profissional, data_inicio__gte=data_atual
    ).order_by("data_inicio")[:25]
