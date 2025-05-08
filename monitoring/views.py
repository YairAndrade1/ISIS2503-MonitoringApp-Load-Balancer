import json
import time
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from alarms.views import create_integrity_alarm
from .utils import verificar_firma
from monitoring.models import Patient
from monitoring.utils import notificar_a_monitor 

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


def crear_paciente(request):
    if request.method == "POST":
        data = json.loads(request.body)
        paciente = Patient.objects.create(
            name=data["name"],
            history=data["history"]
        )
        notificar_a_monitor(paciente)
        return JsonResponse({"message": "Paciente creado"})


def actualizar_paciente(request, id):
    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        paciente = get_object_or_404(Patient, id=id)
        paciente.name = data.get("name", paciente.name)
        paciente.history = data.get("history", paciente.history)
        paciente.save()
        notificar_a_monitor(paciente)
        return JsonResponse({"message": "Paciente actualizado"})


#Revisar los print y si queremos que se verifique en la vista
def verificar_integridad_paciente(patient_id):
    paciente = Patient.objects.get(id=patient_id)
    contenido = f'{paciente.name}|{paciente.history}'
    if verificar_firma(contenido, paciente.digital_signature):
        return "OK: La información no ha sido modificada."
    else:
        create_integrity_alarm(paciente.id, "ALERTA: La historia clínica fue modificada por un tercero.")
        return "ALERTA: La historia clínica fue modificada por un tercero."


def healthCheck(request):
    return HttpResponse('ok')