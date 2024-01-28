from django.contrib import admin
from .models import Piloto, Equipo, Circuito, AvatarImagen

# Register your models here.

admin.site.register(Piloto)
admin.site.register(Equipo)
admin.site.register(Circuito)
admin.site.register(AvatarImagen)
