from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from servicos.decorators import profissional_required
from usuarios.models import Profissional

from .forms import HorarioForm, ResponderAgendamentoForm
from .models import Agendamento, Horario


@profissional_required
def cadastrar_horario(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            horario = form.save(commit=False)
            horario.profissional = Profissional.objects.filter(
                user=request.user,
            ).first()

            horarios_recorrentes = horario.gerar_horarios_recorrentes()
            Horario.objects.bulk_create(horarios_recorrentes)
            return redirect("pagina_inicial")
    else:
        form = HorarioForm()

    context = {"form": form, "is_profissional_autenticado": True}

    return render(request, "cadastrar_horario.html", context=context)


@profissional_required
def listar_horarios(request: HttpRequest, ano=None, mes=None) -> HttpResponse:
    if ano and mes:  # Lista os horários por mês
        horarios = Horario.objects.filter(
            data_inicio__year=ano,
            data_inicio__month=mes,
            profissional__user=request.user,
        ).order_by("data_inicio")
        context = {
            "horarios": horarios,
            "ano": ano,
            "mes": mes,
            "view_type": "detalhes",
            "is_profissional_autenticado": True,
        }

    else:  # Lista o número de horários de cada mês
        resumos_meses = (
            Horario.objects.filter(profissional__user=request.user)
            .annotate(month=TruncMonth("data_inicio"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )

        context = {
            "resumo_meses": resumos_meses,
            "view_type": "resumo",
            "is_profissional_autenticado": True,
        }

    return render(
        request,
        "listar_horarios.html",
        context=context,
    )


@profissional_required
def deletar_horario(request: HttpRequest, pk: int, ano: int, mes: int) -> HttpResponse:
    horario = get_object_or_404(Horario, pk=pk)
    horario.delete()
    return redirect("horarios_detalhes", ano=ano, mes=mes)


def responder_agendamento(request: HttpRequest, id: int) -> HttpResponse:
    agendamento = Agendamento.objects.get(id=id)
    profissional = Profissional.objects.get(id=agendamento.profissional.id)

    if request.method == "POST":
        form = ResponderAgendamentoForm(request.POST, instance=agendamento)

        if form.is_valid():
            novo_status = form.cleaned_data["status"]
            agendamento.status = novo_status
            agendamento.horario.vago = novo_status == "Cancelado"
            agendamento.horario.save()
            agendamento.save()
            return redirect("pagina_perfil", profissional.slug)

    return redirect("pagina_perfil", profissional.slug)
