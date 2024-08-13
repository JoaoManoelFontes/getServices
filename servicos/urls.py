from django.urls import path

from servicos import views

urlpatterns = [
    path("", views.pagina_inicial, name="pagina_inicial"),
]
