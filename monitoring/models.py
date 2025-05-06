from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    # Nuevo campo para la firma
    digital_signature = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
