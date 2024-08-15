from django.db.models import Avg

from avaliacoes.models import Comentario
from usuarios.models import Profissional


def get_avaliacoes(profissional: Profissional) -> dict:
    """Retorna a lista de comentários relacionada a um profissional, bem como a media das avaliacoes"""
    comentarios = (
        Comentario.objects.filter(profissional=profissional)
        .order_by("-created_at")
        .select_related("profissional", "cliente")
    )
    media_avaliacao = comentarios.aggregate(media=Avg("avaliacao"))["media"] or 0

    print(media_avaliacao, comentarios.__len__())

    return {
        "comentarios": comentarios,
        "media_avaliacao": media_avaliacao,
    }
