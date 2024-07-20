import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cliente(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Cliente: " + self.user.username


class Profissional(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    servico = models.ForeignKey("servicos.Servico", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Profissional: " + self.user.username
