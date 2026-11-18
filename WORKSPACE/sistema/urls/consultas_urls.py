from django.urls import path
from sistema.views import consultas_view

urlpatterns = [
    path('consultas/', consultas_view), # vollmed.com/consultas
]