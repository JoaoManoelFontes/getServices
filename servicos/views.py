from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from servicos.decorators import profissional_required
from servicos.forms import HorarioForm
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


@profissional_required
def cadastrar_horario(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = HorarioForm()
    elif request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.profissional = request.user
            form.save()
    return render(
        request,
        "servicos/pages/cadastrar_horario.html",
        {
            "form": form,
        },
    )
