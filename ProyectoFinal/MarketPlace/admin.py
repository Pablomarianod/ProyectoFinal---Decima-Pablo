from django.contrib import admin
from .models import * #importamos el archivo models
# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Categoria)
admin.site.register(Vendedor)