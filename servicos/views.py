from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from servicos.decorators import profissional_required
from servicos.forms import HorarioForm
from usuarios.models import Profissional


# Lista os profissinais na página inicial
def pagina_inicial(request: HttpRequest) -> HttpResponse:
    profissionais = Profissional.objects.all().select_related("user", "servico")

    return render(
        request,
        "servicos/pages/index.html",
        {
            "profissionais": profissionais,
        },
    )


# Realiza o cadastro de um novo horário
@profissional_required
def cadastrar_horario(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        form = HorarioForm()

    elif request.method == "POST":
        form = HorarioForm(request.POST)

        if form.is_valid():
            horario = form.save(commit=False)

            # Atribui o usuário logado ao horário criado
            profissional = Profissional.objects.get(user=request.user)
            horario.profissional = profissional
            horario.save()
            return redirect("pagina_inicial")

    return render(
        request,
        "servicos/pages/cadastrar_horario.html",
        {
            "form": form,
        },
    )
