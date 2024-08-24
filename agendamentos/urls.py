from django.urls import path

from . import views

urlpatterns = [
    path(
        "agendamento/cadastro/<slug:slug>",
        views.cadastrar_agendamento,
        name="cadastrar_agendamento",
    ),
    path(
        "agendamento/responder/<int:id>",
        views.responder_agendamento,
        name="responder_agendamento",
    ),
    path("horarios/cadastro/", views.cadastrar_horario, name="cadastrar_horario"),
    path("horarios/listar/", views.listar_horarios, name="horarios_resumo"),
    path(
        "horarios/listar/<int:ano>/<int:mes>/",
        views.listar_horarios,
        name="horarios_detalhes",
    ),
    path(
        "horarios/deletar/<int:ano>/<int:mes>/<int:pk>/",
        views.deletar_horario,
        name="deletar_horario",
    ),
]
