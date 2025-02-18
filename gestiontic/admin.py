from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Dispositivo, Responsable, Servicio


class ResponsableResource(resources.ModelResource):
    class Meta:
        model = Responsable


class DispositivoResource(resources.ModelResource):
    class Meta:
        model = Dispositivo


class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio


class ResponsableAdmin(ImportExportModelAdmin):
    resource_class = ResponsableResource
    list_display = (
        'id',
        'nombre',
        'apellido',
        'cargo'
    )
    list_filter = ('nombre', 'apellido',)
    # list_per_page = (25)
    # search_fields = ('id',)
    # fieldsets = (
    #     (None, {'fields': ('nombre', 'apellido', 'cargo')}),
    #     ('Relaciones', {'fields': ('dispositivos',)}),
    # )


class DispositivoAdmin(ImportExportModelAdmin):
    resource_class = DispositivoResource
    list_display = (
        'id',
        'activo_nuevo',
        'tipo_dispositivo',
        'marca',
        'modelo',
        'serial',
        'responsable'
    )
    # search_fields = ('activo_nuevo',)
    list_filter = ('activo_nuevo', 'activo_viejo',)
    # fieldsets = (
    #     (None, {'fields': ('serial', 'tipo_dispositivo', 'marca', 'modelo', 'activo_viejo', 'activo_nuevo', 'ubicacion')}),
    #     ('Relaciones', {'fields': ('responsables',)}),
    # )


class ServicioAdmin(ImportExportModelAdmin):
    resource_class = ServicioResource
    list_display = (
        'id',
        'tipo_servicio',
        'requerimiento',
        'solucion',
        'fecha',
        'dispositivos',
    )
    list_filter = ('dispositivos',)
    search_fields = ('dispositivos',)
    # fieldsets = (
    #     (None, {'fields': ('tipo_servicio', 'requerimiento', 'solucion', 'dispositivos',)}),
    #     ('Dispositivos relacionados', {'fields': ()}),
    # )


# Registra tus modelos en el panel de administración
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Servicio, ServicioAdmin)
