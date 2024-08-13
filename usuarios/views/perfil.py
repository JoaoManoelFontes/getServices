from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from usuarios.models import Profissional


def pagina_perfil(request: HttpRequest, slug: str) -> HttpResponse:
    """Exibe o perfil de um profissional."""
    profissional = get_object_or_404(Profissional, slug=slug)
    return render(request, "perfil.html", {"profissional": profissional})
