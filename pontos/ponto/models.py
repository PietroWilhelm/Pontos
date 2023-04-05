from django.db import models
import uuid
import datetime
from usuarios.models import usuarios
# Create your models here.

class ponto(models.Model):
    id_ponto = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    data_ponto = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    def __str__(self):
        nome = usuarios.objects.get(id_usuarios=self.id_usuario)
        return f'{self.data_ponto}'

