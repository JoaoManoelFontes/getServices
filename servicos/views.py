from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from agendamentos import selectors
from agendamentos.models import Agendamento
from servicos.models import Servico
from usuarios.models import Profissional


def pagina_inicial(request: HttpRequest) -> HttpResponse:
    profissionais = (
        Profissional.objects.all()
        .select_related("user", "servico")
        .annotate(media_avaliacao=Avg("avaliacao__nota"))
    )

    agendamentos = Agendamento.objects.filter(cliente__user=request.user)
    servicos = Servico.objects.all()
    agendamentos = []
    horarios = []
    mostrar_cards_profissional = False

    if verificar_user_profissional(request):
        mostrar_cards_profissional = True
        schedule_data = selectors.get_profissional_schedule(request.user.profissional)
        horarios = schedule_data["horarios"]
        agendamentos = schedule_data["agendamentos"]

    return render(
        request,
        "index.html",
        {
            "profissionais": profissionais,
            "servicos": servicos,
            "agendamentos": agendamentos,
            "horarios": horarios,
            "mostrar_cards_profissional": mostrar_cards_profissional,
        },
    )


def verificar_user_profissional(request):
    """Verifica se há um usuário logado e se é um profissional"""
    if request.user.is_authenticated:
        profissional_logado = (
            Profissional.objects.filter(user=request.user)
            .select_related("servico")
            .first()
        )

        return profissional_logado

    return False
