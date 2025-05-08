from django.urls import path
from . import views

app_name = 'verifier'

urlpatterns = [
    path('external-verify/', views.verificar_hash_externo, name='verify_external'),
] 