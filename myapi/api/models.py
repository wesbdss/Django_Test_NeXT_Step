from django.db import models
from django.core.files.base import ContentFile
from django.utils import timezone
# Create your models here.

class person_type(models.Model):
    # Visitante, Empregado, Diretor, Dono, Sócio
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name
    

class person_media_type(models.Model):
    name = models.CharField(max_length=32)
    # id 1 = Foto, id 2 = Biometria
    content = models.IntegerField()
    def __str__(self):
        return self.name
    
class person(models.Model):
    id = models.BigAutoField (primary_key=True)
    name = models.CharField(max_length=32)
    person_type = models.ForeignKey(person_type,on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=32,null=True)
    last_update = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.name

      
# modelo alterado com o proposto
class person_media(models.Model):
    person_id = models.ForeignKey(person,on_delete=models.CASCADE)
    type_media = models.ForeignKey(person_media_type,on_delete=models.CASCADE)
    object_media = models.TextField()

    def __str__(self):
        return self.person_id

class person_audit(models.Model):
    person_id = models.ForeignKey(person,on_delete=models.CASCADE)
    # type = 1 (add) type = 2 (update)
    person_audit_type = models.IntegerField()
    cpf_new = models.CharField(max_length=14)
    cpf_old = models.CharField(max_length=14, null=True)
    last_update = models.DateTimeField()
    def __str__(self):
        return self.cpf_new

