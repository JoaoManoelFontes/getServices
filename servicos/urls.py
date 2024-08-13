from django.urls import path

from servicos import views

urlpatterns = [
    path("", views.pagina_inicial, name="pagina_inicial"),
    path("horario/cadastrar/", views.cadastrar_horario, name="cadastrar_horario"),
]
