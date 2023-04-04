from django.db import models 
import uuid

# Create your models here.

class usuarios(models.Model): 
    id_usuarios = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    cpf_usuario = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name +' '+ self.cpf_usuario