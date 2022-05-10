from django.shortcuts import render

# some_app/views.py
from django.views.generic import TemplateView
from django.views.generic import ListView


class VistaView(TemplateView):
    template_name = "home/vistaview.html"

class HolaMundoView(TemplateView):
    template_name = "home/holamundoview.html"
    
class EjemploListView(ListView):
    template_name = "home/ejemplolistview.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']
    
    