from django.contrib.auth import login
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib import messages
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import LoginForm, RegistrarForm

from .models import Cliente, Profissional
from servicos.models import Servico


class PerfilProfissionalView(DetailView):
    model = Profissional
    template_name = "perfil.html"
    context_object_name = "profissional"
    slug_url_kwarg = "slug"


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

            if servico_id:
                servico = Servico.objects.get(id=servico_id)
                Profissional.objects.create(user=usuario, servico=servico)

        login(self.request, usuario)
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "pagina_login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Nome de usuário ou senha inválidos.")
        return super().form_invalid(form)
