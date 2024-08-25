from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from agendamentos import selectors as agendamentos_selectors
from agendamentos.models import Agendamento
from avaliacoes import selectors as avaliacoes_selectors
from avaliacoes.forms import AvaliacaoForm
from avaliacoes.models import Avaliacao
from servicos.models import Servico

from .forms import LoginForm, RegistrarForm
from .models import Cliente, Profissional


class PerfilProfissionalView(View):
    model = Profissional
    template_name = "perfil.html"

    def get_context_data(self, slug, request):
        profissional = get_object_or_404(Profissional, slug=slug)
        cliente = Cliente.objects.filter(user=request.user).first()

        pode_avaliar = self.usuario_pode_avaliar(
            profissional, cliente, usuario_autenticado=request.user
        )
        print(profissional.servico.nome)
        avaliacoes = self.get_avaliacoes_data(profissional)
        schedule_data = agendamentos_selectors.get_profissional_schedule(profissional)

        horarios = schedule_data["horarios"]

        # TODO: adicionar listagem de agendamentos no template do perfil
        agendamentos = schedule_data["agendamentos"]

        return {
            "profissional": profissional,
            "pode_avaliar": pode_avaliar,
            **avaliacoes,
            "agendamentos": agendamentos,
            "horarios": horarios,
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(self.kwargs.get("slug"), request)
        return render(request, self.template_name, context)

    def post(self, request, slug):
        profissional = get_object_or_404(Profissional, slug=slug)
        cliente = Cliente.objects.get(user=request.user)

        context = self.get_context_data(slug, request)

        if request.POST.get("avaliacao_comentario") and context["pode_avaliar"]:
            form = AvaliacaoForm(request.POST)
            if form.is_valid():
                avaliacao = form.save(commit=False)
                avaliacao.cliente = cliente
                avaliacao.profissional = profissional
                avaliacao.agendamento = Agendamento.objects.filter(
                    cliente=cliente, profissional=profissional, status="Concluido"
                ).first()
                avaliacao.save()
                return redirect("pagina_perfil", slug=profissional.slug)
        else:
            form = AvaliacaoForm()

        context["form"] = form
        return render(request, self.template_name, context)

    def get_avaliacoes_data(self, profissional):
        avaliacoes = avaliacoes_selectors.get_avaliacoes(profissional)

        avaliacoes_notas = (
            avaliacoes["avaliacoes"]
            .values("nota")
            .annotate(count=Count("id"))
            .order_by("-nota")
        )

        total_avaliacoes = len(avaliacoes["avaliacoes"])
        media_avaliacao = avaliacoes["media_avaliacao"]

        return {
            "avaliacoes": avaliacoes["avaliacoes"],
            "media_avaliacao": media_avaliacao,
            "avaliacoes_notas": avaliacoes_notas,
            "total_avaliacoes": total_avaliacoes,
        }

    def usuario_pode_avaliar(self, profissional, cliente, usuario_autenticado):
        if cliente is None or profissional.user == usuario_autenticado:
            return False

        agendamento = Agendamento.objects.filter(
            cliente=cliente, profissional=profissional, status="Concluido"
        ).first()

        pode_avaliar = (
            agendamento is not None
            and not Avaliacao.objects.filter(
                agendamento=agendamento, cliente=cliente
            ).exists()
        )

        return pode_avaliar


class RegistrarView(CreateView):
    form_class = RegistrarForm
    template_name = "pagina_cadastro.html"
    success_url = reverse_lazy("pagina_login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all()
        return context

    def form_valid(self, form):
        usuario = form.save()

        tipo_usuario = self.request.POST.get("tipo_usuario")

        if tipo_usuario == "cliente":
            Cliente.objects.create(user=usuario)
        elif tipo_usuario == "profissional":
            servico_id = self.request.POST.get("servico")
            descricao = self.request.POST.get("descricao")

            if servico_id:
                servico = Servico.objects.get(id=servico_id)
                Profissional.objects.create(
                    user=usuario, servico=servico, descricao=descricao
                )

        login(self.request, usuario)
        return super().form_valid(form)

    def form_invalid(self, form):
        for errors in form.errors.values():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "pagina_login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Nome de usuário ou senha inválidos.")
        return super().form_invalid(form)
