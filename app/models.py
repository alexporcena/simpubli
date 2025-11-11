from django.db import models

class DadosEstado(models.Model):
    json = models.JSONField()
    class Meta:
        db_table = 'dados_estado'

    def __str__(self):
        return f"Registro {self.id}"
