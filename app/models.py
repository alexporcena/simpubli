from django.db import models

class DadosEstado(models.Model):
    json = models.JSONField()
    class Meta:
        db_table = 'dados_estado'

    def __str__(self):
        return f"Registro {self.id}"

class DadosMunicipios(models.Model):
    id = models.AutoField(primary_key=True)
    id_ibge = models.IntegerField()
    json = models.JSONField()
    class Meta:
        db_table = 'dados_municipios'

    def __str__(self):
        return f"Registro {self.id}"
