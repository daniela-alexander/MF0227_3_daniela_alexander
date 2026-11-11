from django.urls import path
from .views import ListaIncidenciasView, CrearIncidenciaView

urlpatterns = [
    path('', ListaIncidenciasView.as_view(), name='lista_incidencias'),
    path('nueva/', CrearIncidenciaView.as_view(), name='crear_incidencia'),
]