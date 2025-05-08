from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    #Nuevo campo para la firma
    digital_signature = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    #Como se guarda
    def save(self, *args, **kwargs):
        from .utils import firmar_contenido
        contenido = f'{self.name}|{self.history}'
        self.digital_signature = firmar_contenido(contenido)
        super().save(*args, **kwargs)

        try:
            requests.post('http://34.9.16.155:5000/verificar-integridad/', json={
                "patient_id": self.id,
                "name": self.name,
                "history": self.history,
                "digital_signature": self.digital_signature
            })
        except Exception as e:
            print(f"[ERROR] No se pudo notificar al monitor: {e}")
