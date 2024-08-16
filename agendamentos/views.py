from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from servicos.decorators import profissional_required
from usuarios.models import Profissional

from .forms import HorarioForm
from .models import Horario


@profissional_required
def cadastrar_horario(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            horario = form.save(commit=False)
            horario.profissional = Profissional.objects.filter(
                user=request.user,
            ).first()
            horario.save()

            horarios_recorrentes = horario.gerar_horarios_recorrentes()
            Horario.objects.bulk_create(horarios_recorrentes)
            return redirect("pagina_inicial")
    else:
        form = HorarioForm()

    return render(request, "cadastrar_horario.html", {"form": form})
