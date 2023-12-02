from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("seguros/", views.insurance, name="insurance"),
    path("alugeis/", views.rent, name="rent"),
    path("vendas/", views.sale, name="sale"),
    path("servicos/", views.service, name="service"),
    path("pagar/<str:contract>/<int:pk>", views.pay, name="pay"),
    path("editar/<str:contract>/<int:pk>", views.edit, name="edit"),
    path("deletar/<str:contract>/<int:pk>", views.delete, name="delete"),
    path("contrato/<str:contract>/<int:pk>", views.print, name="print"),
]
