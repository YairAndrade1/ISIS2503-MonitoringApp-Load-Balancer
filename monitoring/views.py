import time
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
def index(request):
    return render(request, 'index.html')

def consulta_paciente_experimento(request):
    # Simula la latencia requerida (por ejemplo, 300ms)
    time.sleep(0.3)
    data = {
        "id": 123,
        "nombre": "Juan Pérez",
        "edad": 45,
        "diagnosticos": ["epilepsia refractaria"],
        "ultima_consulta": "2025-03-30",
        "mensaje": "Consulta realizada con latencia simulada para el experimento"
    }
    return JsonResponse(data)

def healthCheck(request):
    return HttpResponse('ok')