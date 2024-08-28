from usuarios.models import Profissional


class BaseProfissionalAutenticadoView:
    def get_profissional_autenticado(self):
        return (
            Profissional.objects.filter(user=self.request.user)
            .select_related("servico")
            .first()
            if self.request.user.is_authenticated
            else None
        )
