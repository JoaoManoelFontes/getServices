from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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

    return render(
        request,
        "index.html",
        {
            "profissionais": profissionais,
            "servicos": servicos,
            "agendamentos": agendamentos,
        },
    )
