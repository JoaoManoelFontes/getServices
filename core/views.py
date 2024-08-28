from usuarios.models import Cliente, Profissional


class BaseUsuarioAutenticadoView:
    def get_profissional_autenticado(self):
        return (
            Profissional.objects.filter(user=self.request.user)
            .select_related("servico")
            .first()
            if self.request.user.is_authenticated
            else None
        )

    def get_cliente_autenticado(self):
        return (
            Cliente.objects.filter(user=self.request.user).first()
            if self.request.user.is_authenticated
            else None
        )
