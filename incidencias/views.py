from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Incidencia
from .forms import IncidenciaForm

class ListaIncidenciasView(ListView):
    model = Incidencia
    template_name = 'incidencias/lista.html'
    context_object_name = 'incidencias'

class CrearIncidenciaView(CreateView):
    model = Incidencia
    form_class = IncidenciaForm
    template_name = 'incidencias/formulario.html'
    success_url = reverse_lazy('lista_incidencias')