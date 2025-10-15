# api_clinica/forms.py
from django import forms
from .models import Especialidad, Medico, Paciente, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica, Enfermera

"""
    Definición de formularios Django para cada modelo.
    Estos formularios se utilizan en las vistas basadas en plantillas (HTML)
    para crear y actualizar instancias de los modelos.
"""

class EspecialidadForm(forms.ModelForm):
    """
        Formulario para el modelo Especialidad.
        Permite crear y editar especialidades médicas.
    """
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion'] # Campos a incluir en el formulario
        labels = { # Etiquetas personalizadas para los campos
            'nombre': 'Nombre de la Especialidad',
            'descripcion': 'Descripción',
        }
        widgets = { # Widgets personalizados para los campos (ej. Textarea para descripción)
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MedicoForm(forms.ModelForm):
    """
        Formulario para el modelo Medico.
        Permite crear y editar información de médicos.
    """
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo', 'especialidad']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'activo': 'Activo',
            'especialidad': 'Especialidad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}), # Selector para ForeignKey
        }

class PacienteForm(forms.ModelForm):
    """
        Formulario para el modelo Paciente.
        Permite crear y editar información de pacientes.
    """
    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'tipo_sangre', 'correo', 'telefono', 'direccion', 'activo']
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'tipo_sangre': 'Tipo de Sangre',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'activo': 'Activo',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # Input de fecha HTML5
            'tipo_sangre': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ConsultaMedicaForm(forms.ModelForm):
    """
        Formulario para el modelo ConsultaMedica.
        Permite programar y actualizar consultas médicas.
    """
    class Meta:
        model = ConsultaMedica
        fields = ['paciente', 'medico', 'fecha_consulta', 'motivo', 'diagnostico', 'estado']
        labels = {
            'paciente': 'Paciente',
            'medico': 'Médico',
            'fecha_consulta': 'Fecha y Hora de la Consulta',
            'motivo': 'Motivo de la Consulta',
            'diagnostico': 'Diagnóstico',
            'estado': 'Estado',
        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'fecha_consulta': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}), # Input de fecha y hora HTML5
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class TratamientoForm(forms.ModelForm):
    """
        Formulario para el modelo Tratamiento.
        Permite registrar y actualizar tratamientos asociados a una consulta.
    """
    class Meta:
        model = Tratamiento
        fields = ['consulta', 'descripcion', 'duracion_dias', 'observaciones']
        labels = {
            'consulta': 'Consulta Médica',
            'descripcion': 'Descripción del Tratamiento',
            'duracion_dias': 'Duración (días)',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'consulta': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion_dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MedicamentoForm(forms.ModelForm):
    """
        Formulario para el modelo Medicamento.
        Permite gestionar el inventario de medicamentos.
    """
    class Meta:
        model = Medicamento
        fields = ['nombre', 'laboratorio', 'stock', 'precio_unitario']
        labels = {
            'nombre': 'Nombre del Medicamento',
            'laboratorio': 'Laboratorio',
            'stock': 'Stock Disponible',
            'precio_unitario': 'Precio Unitario',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'laboratorio': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), # Permite valores decimales
        }

class RecetaMedicaForm(forms.ModelForm):
    """
        Formulario para el modelo RecetaMedica.
        Permite crear y actualizar recetas médicas para tratamientos.
    """
    class Meta:
        model = RecetaMedica
        fields = ['tratamiento', 'medicamento', 'dosis', 'frecuencia', 'duracion']
        labels = {
            'tratamiento': 'Tratamiento Asociado',
            'medicamento': 'Medicamento',
            'dosis': 'Dosis',
            'frecuencia': 'Frecuencia',
            'duracion': 'Duración',
        }
        widgets = {
            'tratamiento': forms.Select(attrs={'class': 'form-control'}),
            'medicamento': forms.Select(attrs={'class': 'form-control'}),
            'dosis': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EnfermeraForm(forms.ModelForm):
    """
        Formulario para el modelo Enfermera.
        Permite crear y editar información de enfermeras.
    """
    class Meta:
        model = Enfermera
        fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'activo', 'medico_a_cargo']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'rut': 'RUT',
            'correo': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'activo': 'Activo',
            'medico_a_cargo': 'Médico a Cargo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'medico_a_cargo': forms.Select(attrs={'class': 'form-control'}), # Selector para ForeignKey
        }