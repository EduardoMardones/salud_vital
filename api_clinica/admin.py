# api_clinica/admin.py
from django.contrib import admin
from .models import Especialidad, Medico, Paciente, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica

"""
    Configuración del panel de administración de Django para los modelos de la clínica.
    Esto permite gestionar los datos de forma sencilla a través de la interfaz de administración.
"""

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    """
        Administración para el modelo Especialidad.
        Muestra 'nombre' y 'descripcion' en la lista, permite buscar por 'nombre'.
    """
    list_display = ('nombre', 'descripcion') # Campos a mostrar en la lista de objetos
    search_fields = ('nombre',) # Campos por los cuales se puede buscar


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    """
        Administración para el modelo Medico.
        Muestra campos clave en la lista, permite buscar por nombre, apellido, RUT y correo.
        Permite filtrar por especialidad y estado 'activo'.
    """
    list_display = ('nombre', 'apellido', 'rut', 'correo', 'especialidad', 'activo') # Campos a mostrar
    search_fields = ('nombre', 'apellido', 'rut', 'correo') # Campos para búsqueda
    list_filter = ('especialidad', 'activo') # Filtros laterales
    raw_id_fields = ('especialidad',) # Para campos ForeignKey, permite seleccionar mediante un popup de ID


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    """
        Administración para el modelo Paciente.
        Muestra campos clave en la lista, permite buscar por nombre, apellido y RUT.
        Permite filtrar por tipo de sangre y estado 'activo'.
    """
    list_display = ('nombre', 'apellido', 'rut', 'fecha_nacimiento', 'tipo_sangre', 'activo') # Campos a mostrar
    search_fields = ('nombre', 'apellido', 'rut') # Campos para búsqueda
    list_filter = ('tipo_sangre', 'activo') # Filtros laterales
    date_hierarchy = 'fecha_nacimiento' # Navegación jerárquica por fecha


@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    """
        Administración para el modelo ConsultaMedica.
        Muestra información clave de la consulta, permite buscar por motivo y diagnóstico.
        Permite filtrar por médico, paciente y estado.
    """
    list_display = ('paciente', 'medico', 'fecha_consulta', 'estado', 'diagnostico') # Campos a mostrar
    search_fields = ('motivo', 'diagnostico', 'paciente__nombre', 'medico__nombre') # Búsqueda en campos relacionados
    list_filter = ('estado', 'medico', 'paciente', 'fecha_consulta') # Filtros laterales
    raw_id_fields = ('paciente', 'medico') # Para campos ForeignKey
    date_hierarchy = 'fecha_consulta' # Navegación jerárquica por fecha


@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    """
        Administración para el modelo Tratamiento.
        Muestra el ID de la consulta, duración y descripción.
        Permite buscar por descripción.
    """
    list_display = ('consulta', 'descripcion', 'duracion_dias') # Campos a mostrar
    search_fields = ('descripcion', 'consulta__paciente__nombre', 'consulta__medico__nombre') # Búsqueda en campos relacionados
    raw_id_fields = ('consulta',) # Para campos ForeignKey


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    """
        Administración para el modelo Medicamento.
        Muestra nombre, laboratorio, stock y precio.
        Permite buscar por nombre y laboratorio.
        Permite filtrar por laboratorio.
    """
    list_display = ('nombre', 'laboratorio', 'stock', 'precio_unitario') # Campos a mostrar
    search_fields = ('nombre', 'laboratorio') # Campos para búsqueda
    list_filter = ('laboratorio',) # Filtros laterales
    list_editable = ('stock', 'precio_unitario') # Permite editar estos campos directamente desde la lista


@admin.register(RecetaMedica)
class RecetaMedicaAdmin(admin.ModelAdmin):
    """
        Administración para el modelo RecetaMedica.
        Muestra el tratamiento, medicamento, dosis y frecuencia.
        Permite buscar por dosis y frecuencia.
    """
    list_display = ('tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion') # Campos a mostrar
    search_fields = ('dosis', 'frecuencia', 'medicamento__nombre') # Búsqueda en campos relacionados
    raw_id_fields = ('tratamiento', 'medicamento') # Para campos ForeignKey