from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from usuarios.models import Profissional


# Create your views here.
def pagina_inicial(request: HttpRequest) -> HttpResponse:
    profissionais = Profissional.objects.all().select_related("user", "servico")

    return render(
        request,
        "servicos/pages/index.html",
        {
            "profissionais": profissionais,
        },
    )
