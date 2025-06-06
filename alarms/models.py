from django.db import models
from variables.models import Variable
from measurements.models import Measurement

class Alarm(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"variable": %s, "measurement": %s, "limitExceeded": %s, "dateTime": %s}' % (self.variable.name, self.measurement.value, self.limitExceeded, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'variable': self.variable.name,
            'measurement': self.measurement.value,
            'value': self.value,
            'dateTime': self.dateTime,
            'limitExceeded': self.limitExceeded
        }
        return alarm
    
class IntegrityAlarm(models.Model):
    patient_id = models.IntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] Paciente {self.patient_id}: {self.message}"

    def toJson(self):
        return {
            "patient_id": self.patient_id,
            "message": self.message,
            "timestamp": self.timestamp
        }
    class Meta:
        db_table = 'alarms_integrityalarm'
