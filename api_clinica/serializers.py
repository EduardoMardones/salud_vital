# api_clinica/serializers.py
from rest_framework import serializers
from .models import Especialidad, Medico, Paciente, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica, Enfermera

# Serializador para el modelo Especialidad
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__' # Incluye todos los campos del modelo

# Serializador para el modelo Medico
# Incluye la especialidad como un campo anidado para mostrar su nombre
class MedicoSerializer(serializers.ModelSerializer):
    especialidad_nombre = serializers.CharField(source='especialidad.nombre', read_only=True) # Muestra el nombre de la especialidad

    class Meta:
        model = Medico
        fields = '__all__' # Incluye todos los campos del modelo
        # fields = ['id', 'nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo', 'especialidad', 'especialidad_nombre']

# Serializador para el modelo Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__' # Incluye todos los campos del modelo

# Serializador para el modelo ConsultaMedica
# Incluye el nombre del paciente y del médico para una mejor visualización
class ConsultaMedicaSerializer(serializers.ModelSerializer):
    paciente_nombre_completo = serializers.SerializerMethodField() # Campo calculado para el nombre completo del paciente
    medico_nombre_completo = serializers.SerializerMethodField() # Campo calculado para el nombre completo del médico

    class Meta:
        model = ConsultaMedica
        fields = '__all__'
        # fields = ['id', 'paciente', 'paciente_nombre_completo', 'medico', 'medico_nombre_completo', 'fecha_consulta', 'motivo', 'diagnostico', 'estado']

    # Método para obtener el nombre completo del paciente
    def get_paciente_nombre_completo(self, obj):
        return f"{obj.paciente.nombre} {obj.paciente.apellido}"

    # Método para obtener el nombre completo del médico
    def get_medico_nombre_completo(self, obj):
        return f"{obj.medico.nombre} {obj.medico.apellido}"

# Serializador para el modelo Tratamiento
# Incluye el ID de la consulta médica relacionada
class TratamientoSerializer(serializers.ModelSerializer):
    consulta_id = serializers.PrimaryKeyRelatedField(source='consulta', read_only=True) # Muestra el ID de la consulta

    class Meta:
        model = Tratamiento
        fields = '__all__'
        # fields = ['id', 'consulta', 'consulta_id', 'descripcion', 'duracion_dias', 'observaciones']

# Serializador para el modelo Medicamento
class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

# Serializador para el modelo RecetaMedica
# Incluye el nombre del medicamento y el ID del tratamiento
class RecetaMedicaSerializer(serializers.ModelSerializer):
    medicamento_nombre = serializers.CharField(source='medicamento.nombre', read_only=True) # Muestra el nombre del medicamento
    tratamiento_id = serializers.PrimaryKeyRelatedField(source='tratamiento', read_only=True) # Muestra el ID del tratamiento

    class Meta:
        model = RecetaMedica
        fields = '__all__'
        # fields = ['id', 'tratamiento', 'tratamiento_id', 'medicamento', 'medicamento_nombre', 'dosis', 'frecuencia', 'duracion']

class EnfermeraSerializer(serializers.ModelSerializer):
    medico_a_cargo_nombre_completo = serializers.SerializerMethodField()
    # Opcional: si quieres el ID del médico a cargo en la salida, pero ya está incluido en fields='__all__'
    # medico_a_cargo_id = serializers.PrimaryKeyRelatedField(source='medico_a_cargo', read_only=True)

    class Meta:
        model = Enfermera
        fields = '__all__'
        # Si prefieres especificar los campos explícitamente:
        # fields = [
        #     'id', 'nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo',
        #     'medico_a_cargo', 'medico_a_cargo_nombre_completo'
        # ]

    def get_medico_a_cargo_nombre_completo(self, obj):
        if obj.medico_a_cargo: # Verifica si hay un médico asignado
            return f"{obj.medico_a_cargo.nombre} {obj.medico_a_cargo.apellido}"
        return None # Retorna None si no hay un médico asignado