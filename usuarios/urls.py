from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import LoginView, PerfilProfissionalView, RegistrarView

urlpatterns = [
    path("cadastrar", RegistrarView.as_view(), name="pagina_cadastro"),
    path("login", LoginView.as_view(), name="pagina_login"),
    path("logout", LogoutView.as_view(), name="pagina_logout"),
    path("perfil/<slug:slug>/", PerfilProfissionalView.as_view(), name="pagina_perfil"),
]
