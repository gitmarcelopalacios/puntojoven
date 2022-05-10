from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import VistaView, HolaMundoView, EjemploListView


# urls.py

urlpatterns = [
    path('vista/', VistaView.as_view()),
    path('holamundo/', HolaMundoView.as_view()),
    path('ejemplolistview/', EjemploListView.as_view()),
]