import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.FileField(upload_to="users/%y/%m/%d", null=True, blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Cliente(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Cliente: " + self.user.username


class Profissional(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    servico = models.ForeignKey("servicos.Servico", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Profissionais"

    def __str__(self) -> str:
        return "Profissional: " + self.user.username

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.slug = slugify(self.user.username)
        super().save(force_insert, force_update, using, update_fields)
