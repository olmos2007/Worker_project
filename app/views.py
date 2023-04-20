from django.shortcuts import render

from .models import Bolimlar, Hodimlar, Malumoti, Qarindoshlar

from django.views.generic import ListView

class HodimlarView(ListView):
    model = Hodimlar
    template_name = 'index.html'
    context_object_name = 'Hodim'

