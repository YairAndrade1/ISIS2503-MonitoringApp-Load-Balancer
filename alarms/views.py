from django.http import JsonResponse
from django.shortcuts import render

from variables.logic.variable_logic import get_variable_by_id
from .logic.logic_alarm import get_alarms, get_measurements_by_variable, create_alarm
from alarms.models import IntegrityAlarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, variable_id):
    variable = get_variable_by_id(variable_id)
    measurements = get_measurements_by_variable(variable_id)
    createAlarm = False
    upperMeasurement = None
    for measurement in measurements:
        if measurement.value >= 30:
            createAlarm = True
            upperMeasurement = measurement
    if createAlarm:
        alarm = create_alarm(variable, upperMeasurement, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)
    

def create_integrity_alarm(patient_id, message):
    alarm = IntegrityAlarm.objects.create(
        patient_id=patient_id,
        message=message
    )
    return alarm


def integrity_alarm_list(request):
    alarms = IntegrityAlarm.objects.all().order_by('-timestamp')
    context = [a.toJson() for a in alarms]
    return JsonResponse(context, safe=False)