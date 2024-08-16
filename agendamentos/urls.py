from django.urls import path

from . import views

urlpatterns = [
    path("horarios/cadastro/", views.cadastrar_horario, name="cadastrar_horario"),
]
