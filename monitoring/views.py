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
    patient = get_object_or_404(Patient, id=1)  
    
    # Simula la latencia extra de ~18ms
    time.sleep(0.018)  # 3% de 600ms
    
    # Si usas la BD, podrías hacer algo como:
    data = {
        "patient_id": patient.id,
        "name": patient.name,
        "history": patient.history
    }

    return JsonResponse(data)

def healthCheck(request):
    return HttpResponse('ok')