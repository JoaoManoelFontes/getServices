from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from usuarios.forms import BaseUserForm, ClienteForm, ProfissionalForm


def cadastrar_cliente(request: HttpRequest) -> HttpResponse:
    """Realiza o cadastro de um novo cliente."""
    if request.method == "POST":
        base_user_form = BaseUserForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if base_user_form.is_valid() and cliente_form.is_valid():
            base_user = base_user_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = base_user
            cliente.save()
            return render(
                request,
                "home",
                {"mensagem": "Cliente cadastrado com sucesso!"},
            )

        return render(
            request,
            "cadastro.html",
            {
                "base_user_form": base_user_form,
                "cliente_form": cliente_form,
            },
        )

    base_user_form = BaseUserForm()
    cliente_form = ClienteForm()
    return render(request, "cadastro.html")


def cadastrar_profissional(request: HttpRequest) -> HttpResponse:
    """Realiza o cadastro de um novo profissional."""
    if request.method == "POST":
        base_user_form = BaseUserForm(request.POST)
        profissional_form = ProfissionalForm(request.POST)

        if base_user_form.is_valid() and profissional_form.is_valid():
            base_user = base_user_form.save()
            profissional = profissional_form.save(commit=False)
            profissional.user = base_user
            profissional.save()
            return render(
                request,
                "home",
                {"mensagem": "Profissional cadastrado com sucesso!"},
            )

        return render(
            request,
            "cadastro.html",
            {
                "base_user_form": base_user_form,
                "profissional_form": profissional_form,
            },
        )

    base_user_form = BaseUserForm()
    profissional_form = ProfissionalForm()
    return render(request, "cadastro.html")
