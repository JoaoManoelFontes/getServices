from django.db.models import Avg, F, Value
from django.db.models.functions import Concat
from django.views.generic import ListView

from agendamentos import selectors
from core.views import BaseUsuarioAutenticadoView
from servicos.models import Servico
from usuarios.models import Profissional


class PaginaInicialView(ListView, BaseUsuarioAutenticadoView):
    model = Profissional
    template_name = "index.html"
    context_object_name = "profissionais"

    def get_queryset(self):
        queryset = (
            Profissional.objects.all()
            .select_related("user", "servico")
            .annotate(media_avaliacao=Avg("avaliacao__nota"))
        )

        servico_id = self.request.GET.get("servico")
        if servico_id and servico_id != "todos":
            servico = Servico.objects.get(id=servico_id)
            queryset = queryset.filter(servico=servico)

        nome_profissional = self.request.GET.get("profissional")
        if nome_profissional:
            queryset = queryset.annotate(
                nome=Concat(F("user__first_name"), Value(" "), F("user__last_name"))
            ).filter(nome__icontains=nome_profissional)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all()
        context["is_profissional_autenticado"] = False
        context["is_cliente_autenticado"] = False

        profissional_autenticado = self.get_profissional_autenticado()
        cliente_autenticado = self.get_cliente_autenticado()

        if profissional_autenticado:
            context["is_profissional_autenticado"] = True
            schedule_data = selectors.get_profissional_schedule(
                profissional_autenticado
            )
            context["meus_horarios"] = schedule_data["horarios"]
            context["meus_agendamentos"] = schedule_data["agendamentos"]
        elif cliente_autenticado:
            context["is_cliente_autenticado"] = True
            schedule_data = selectors.get_cliente_schedule(cliente_autenticado)
            context["meus_agendamentos"] = schedule_data["agendamentos"]

        return context
