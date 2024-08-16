from django.contrib import admin

from .models import Horario


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
