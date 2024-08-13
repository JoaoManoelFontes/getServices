from django.urls import path

from .views.perfil import perfil

urlpatterns = [
    path("perfil/<slug:slug>/", perfil, name="perfil"),
]
