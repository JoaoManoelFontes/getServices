from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from usuarios.models import Profissional


def pagina_inicial(request: HttpRequest) -> HttpResponse:
    profissionais = (
        Profissional.objects.all()
        .select_related("user", "servico")
        .annotate(media_avaliacao=Avg("avaliacao__nota"))
    )

    return render(
        request,
        "index.html",
        {"profissionais": profissionais},
    )
