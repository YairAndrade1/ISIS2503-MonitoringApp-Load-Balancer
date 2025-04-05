from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()

    def __str__(self):
        return self.name
