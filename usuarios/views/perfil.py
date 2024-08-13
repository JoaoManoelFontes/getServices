from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from usuarios.models import Profissional


def perfil(request: HttpRequest, slug: str) -> HttpResponse:
    """Exibe o perfil de um profissional."""
    usuario = get_object_or_404(Profissional, slug=slug)
    return render(request, "usuarios/pages/perfil.html", {"profissional": usuario})
