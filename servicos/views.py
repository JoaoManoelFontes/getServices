from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from usuarios.models import Profissional


def pagina_inicial(request: HttpRequest) -> HttpResponse:
    profissionais = Profissional.objects.all().select_related("user", "servico")

    return render(
        request,
        "index.html",
        {
            "profissionais": profissionais,
        },
    )
