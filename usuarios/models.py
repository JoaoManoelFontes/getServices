import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


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
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name_plural = "Profissionais"

    def __str__(self) -> str:
        return "Profissional: " + self.user.username

    def save(self, *args: any, **kwargs: any) -> None:
        if not self.slug:
            self.slug = slugify(
                self.user.username,
            )
        super().save(*args, **kwargs)
