import time
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from monitoring.models import Patient
def index(request):
    return render(request, 'index.html')

def patient_history(request):
    """
    Simula la consulta de la historia de un paciente.
    Agrega 3% de latencia adicional sobre 600ms (aprox. 18ms).
    """
    # Si quieres hacer una consulta real a la BD:
    # patient = get_object_or_404(Patient, id=1)  # O el id que necesites
    
    # Respuesta de ejemplo (si no usas BD real):
    data = {
        "patient_id": 1,
        "name": "John Doe",
        "history": "Historial clínico simulado."
    }
    
    # Si usas la BD, podrías hacer algo como:
    # data = {
    #     "patient_id": patient.id,
    #     "name": patient.name,
    #     "history": patient.history
    # }

    return JsonResponse(data)

def healthCheck(request):
    return HttpResponse('ok')