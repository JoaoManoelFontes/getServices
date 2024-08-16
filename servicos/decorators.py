from functools import wraps

from django.http import HttpResponseForbidden


def profissional_required(view_func: any) -> any:
    @wraps(view_func)
    def _wrapped_view(request: any, *args: tuple, **kwargs: dict) -> any:
        if hasattr(request.user, "profissional"):
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    return _wrapped_view
