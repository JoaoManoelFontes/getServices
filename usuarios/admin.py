from django.contrib import admin

from usuarios.models import BaseUser, Cliente, Profissional

# Register your models here.
admin.site.register(Profissional)
admin.site.register(Cliente)
admin.site.register(BaseUser)
