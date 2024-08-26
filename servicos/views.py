from django.db.models import Avg, Q
from django.views.generic import ListView

from agendamentos import selectors
from servicos.models import Servico
from usuarios.models import Profissional


class PaginaInicialView(ListView):
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
            queryset = queryset.filter(
                Q(user__first_name__icontains=nome_profissional)
                | Q(user__last_name__icontains=nome_profissional)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all()
        context["agendamentos"] = []
        context["horarios"] = []
        context["is_profissional_autenticado"] = False

        profissional_autenticado = self.get_profissional_autenticado()

        if profissional_autenticado:
            context["is_profissional_autenticado"] = True
            schedule_data = selectors.get_profissional_schedule(
                profissional_autenticado
            )
            context["horarios"] = schedule_data["horarios"]
            context["agendamentos"] = schedule_data["agendamentos"]

        return context

    def get_profissional_autenticado(self):
        return (
            Profissional.objects.filter(user=self.request.user)
            .select_related("servico")
            .first()
            if self.request.user.is_authenticated
            else None
        )
