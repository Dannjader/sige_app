from .models import Responsable, Dispositivo, Servicio
from import_export import resources


class ResponsableResource(resources.ModelResource):
    class Meta:
        model = Responsable
        fields = (
            'id',
            'nombre',
            'apellido',
            'cargo'
        )
        import_id_fields = ('id',)


class DispositivoResource(resources.ModelResource):
    class Meta:
        model = Dispositivo
        fields = (
            'id',
            'serial',
            'tipo_dispositivo',
            'marca',
            'modelo',
            'activo_viejo',
            'activo_nuevo',
            'ubicacion'
        )
        import_id_fields = ('id',)


class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio
        fields = (
            'id',
            'tipo_servicio',
            'requerimiento',
            'solucion',
            'fecha',
            'dispositivos'
        )
        import_id_fields = ('id',)
