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
        #nome = self.objects.get(primary_key=self.id_usuario)
        return self.data_ponto

