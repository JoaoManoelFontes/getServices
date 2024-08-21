from django.contrib import admin

from .models import Agendamento, Horario


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = (
        "data_inicio",
        "data_fim",
        "vago",
        "frequencia",
        "dias_semana",
        "data_fim_recorrencia",
    )
    ordering = ("-data_inicio",)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = (
        "profissional",
        "cliente",
        "horario",
        "status",
        "created_at",
    )
    ordering = ("-created_at",)
