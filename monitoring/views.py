import time
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from monitoring.models import Patient
def index(request):
    return render(request, 'index.html')

from django.core.cache import cache

def patient_history(request):
    data = cache.get('patient_1')
    if not data:
        patient = get_object_or_404(Patient, id=1)
        data = {
            "patient_id": patient.id,
            "name": patient.name,
            "history": patient.history
        }
        cache.set('patient_1', data, timeout=60) 
    return JsonResponse(data)


def healthCheck(request):
    return HttpResponse('ok')