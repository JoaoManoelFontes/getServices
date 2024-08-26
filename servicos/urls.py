from django.urls import path

from servicos import views

urlpatterns = [
    path("", views.PaginaInicialView.as_view(), name="pagina_inicial"),
]
