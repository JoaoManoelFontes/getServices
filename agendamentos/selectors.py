from django.utils import timezone

from usuarios.models import Profissional

from .models import Horario


def get_horarios(profissional: Profissional):
    return Horario.objects.filter(
        profissional=profissional, data_inicio__gte=timezone.now()
    ).order_by("data_inicio")
