from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from usuarios.forms import BaseUserForm, ClienteForm


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
