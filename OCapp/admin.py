from django.contrib import admin
from .models import Sector, Orden, Cuit

# Register your models here.

class SectorAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')

class OrdenAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')


class CuitAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')

admin.site.register(Sector, SectorAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Cuit, CuitAdmin)
