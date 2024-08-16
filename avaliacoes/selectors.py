from django.db.models import Avg

from avaliacoes.models import Avaliacao
from usuarios.models import Profissional


def get_avaliacoes(profissional: Profissional) -> dict:
    """Retorna a lista de comentários relacionada a um profissional, bem como a media das avaliacoes"""
    avaliacoes = (
        Avaliacao.objects.filter(profissional=profissional)
        .order_by("-created_at")
        .select_related("profissional", "cliente__user")
    )

    media_avaliacao = avaliacoes.aggregate(media=Avg("nota"))["media"] or 0

    return {
        "avaliacoes": avaliacoes,
        "media_avaliacao": media_avaliacao,
    }
