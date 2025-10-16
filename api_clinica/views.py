from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q # Para filtros y búsquedas
from rest_framework import generics # Para las vistas de la API REST
from rest_framework import viewsets


# Importar todos los modelos, incluyendo Enfermera
from .models import Especialidad, Medico, Paciente, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica, Enfermera
# Importar todos los serializadores, incluyendo EnfermeraSerializer
from .serializers import EspecialidadSerializer, MedicoSerializer, PacienteSerializer, ConsultaMedicaSerializer, \
    TratamientoSerializer, MedicamentoSerializer, RecetaMedicaSerializer, EnfermeraSerializer
# Importar todos los formularios, incluyendo EnfermeraForm (¡recuerda crear este!)
from .forms import EspecialidadForm, MedicoForm, PacienteForm, ConsultaMedicaForm, TratamientoForm, \
    MedicamentoForm, RecetaMedicaForm, EnfermeraForm




# ViewSet para Especialidad
class EspecialidadViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las especialidades ser vistas o editadas.
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

# ViewSet para Medico
class MedicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los médicos ser vistos o editados.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

# ViewSet para Paciente
class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los pacientes ser vistos o editados.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# ViewSet para ConsultaMedica
class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las consultas médicas ser vistas o editadas.
    """
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

# ViewSet para Tratamiento
class TratamientoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los tratamientos ser vistos o editados.
    """
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

# ViewSet para Medicamento
class MedicamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los medicamentos ser vistos o editados.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

# ViewSet para RecetaMedica
class RecetaMedicaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las recetas médicas ser vistas o editadas.
    """
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer

# ViewSet para Enfermera
class EnfermeraViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las enfermeras ser vistas o editadas.
    """
    queryset = Enfermera.objects.all()
    serializer_class = EnfermeraSerializer

"""
    Este archivo contiene todas las vistas para la aplicación 'api_clinica'.
    Incluye vistas para la API RESTful (utilizando Django REST Framework)
    y vistas basadas en plantillas (HTML, CSS, Bootstrap) para un CRUD completo.
"""

# Vistas para la API RESTful (Django REST Framework)
# ======================================================================================================================

class EspecialidadListCreate(generics.ListCreateAPIView):
    """
        API para listar todas las especialidades o crear una nueva.
        Utiliza EspecialidadSerializer para la serialización de datos.
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar una especialidad específica por su ID.
        Utiliza EspecialidadSerializer para la serialización de datos.
    """
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class MedicoListCreate(generics.ListCreateAPIView):
    """
        API para listar todos los médicos o crear uno nuevo.
        Permite filtrar médicos por especialidad_id.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_queryset(self):
        # Permite filtrar médicos por el ID de la especialidad (ej: /api/medicos/?especialidad=1)
        queryset = super().get_queryset()
        especialidad_id = self.request.query_params.get('especialidad', None)
        if especialidad_id:
            queryset = queryset.filter(especialidad__id=especialidad_id)
        return queryset

class MedicoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar un médico específico por su ID.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteListCreate(generics.ListCreateAPIView):
    """
        API para listar todos los pacientes o crear uno nuevo.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar un paciente específico por su ID.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaMedicaListCreate(generics.ListCreateAPIView):
    """
        API para listar todas las consultas médicas o crear una nueva.
        Permite filtrar consultas por paciente_id, medico_id y estado.
    """
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        paciente_id = self.request.query_params.get('paciente', None)
        medico_id = self.request.query_params.get('medico', None)
        estado = self.request.query_params.get('estado', None)

        if paciente_id:
            queryset = queryset.filter(paciente__id=paciente_id)
        if medico_id:
            queryset = queryset.filter(medico__id=medico_id)
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset


class ConsultaMedicaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar una consulta médica específica por su ID.
    """
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class TratamientoListCreate(generics.ListCreateAPIView):
    """
        API para listar todos los tratamientos o crear uno nuevo.
        Permite filtrar tratamientos por consulta_id.
    """
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        consulta_id = self.request.query_params.get('consulta', None)
        if consulta_id:
            queryset = queryset.filter(consulta__id=consulta_id)
        return queryset

class TratamientoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar un tratamiento específico por su ID.
    """
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoListCreate(generics.ListCreateAPIView):
    """
        API para listar todos los medicamentos o crear uno nuevo.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar un medicamento específico por su ID.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaMedicaListCreate(generics.ListCreateAPIView):
    """
        API para listar todas las recetas médicas o crear una nueva.
        Permite filtrar recetas por tratamiento_id y medicamento_id.
    """
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        tratamiento_id = self.request.query_params.get('tratamiento', None)
        medicamento_id = self.request.query_params.get('medicamento', None)

        if tratamiento_id:
            queryset = queryset.filter(tratamiento__id=tratamiento_id)
        if medicamento_id:
            queryset = queryset.filter(medicamento__id=medicamento_id)
        return queryset

class RecetaMedicaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar una receta médica específica por su ID.
    """
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer

# --- NUEVAS VISTAS PARA EL MODELO ENFERMERA (API RESTful) ---
class EnfermeraListCreate(generics.ListCreateAPIView):
    """
        API para listar todas las enfermeras o crear una nueva.
        Permite filtrar enfermeras por medico_a_cargo_id.
    """
    queryset = Enfermera.objects.all()
    serializer_class = EnfermeraSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        medico_id = self.request.query_params.get('medico_a_cargo', None)
        if medico_id:
            queryset = queryset.filter(medico_a_cargo__id=medico_id)
        return queryset

class EnfermeraRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API para recuperar, actualizar o eliminar una enfermera específica por su ID.
    """
    queryset = Enfermera.objects.all()
    serializer_class = EnfermeraSerializer
# -----------------------------------------------------------


# Vistas basadas en plantillas (HTML, CSS, Bootstrap)
# ======================================================================================================================

def home(request):
    """
        Vista para la página de inicio o dashboard.
        Renderiza la plantilla 'home.html'.
    """
    return render(request, 'api_clinica/home.html')

# Vistas CRUD para Especialidad (sin cambios)
def especialidad_list(request):
    query = request.GET.get('q')
    if query:
        especialidades = Especialidad.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    else:
        especialidades = Especialidad.objects.all()
    return render(request, 'api_clinica/especialidad/especialidad_list.html', {'especialidades': especialidades, 'query': query})

def especialidad_create(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especialidad creada exitosamente!')
            return redirect('web_especialidad_list')
    else:
        form = EspecialidadForm()
    return render(request, 'api_clinica/especialidad/especialidad_form.html', {'form': form, 'action': 'Crear'})

def especialidad_update(request, pk):
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Especialidad actualizada exitosamente!')
            return redirect('web_especialidad_list')
    else:
        form = EspecialidadForm(instance=especialidad)
    return render(request, 'api_clinica/especialidad/especialidad_form.html', {'form': form, 'action': 'Editar'})

def especialidad_delete(request, pk):
    especialidad = get_object_or_404(Especialidad, pk=pk)
    if request.method == 'POST':
        especialidad.delete()
        messages.success(request, 'Especialidad eliminada exitosamente!')
        return redirect('web_especialidad_list')
    return render(request, 'api_clinica/especialidad/especialidad_confirm_delete.html', {'especialidad': especialidad})

# Vistas CRUD para Paciente (sin cambios)
def paciente_list(request):
    pacientes = Paciente.objects.all()
    query = request.GET.get('q')
    tipo_sangre_filter = request.GET.get('tipo_sangre')
    activo_filter = request.GET.get('activo')

    if query:
        pacientes = pacientes.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(rut__icontains=query))

    if tipo_sangre_filter:
        pacientes = pacientes.filter(tipo_sangre=tipo_sangre_filter)
    
    if activo_filter is not None:
        pacientes = pacientes.filter(activo=(activo_filter == 'true'))

    tipo_sangre_choices = Paciente.TIPO_SANGRE_CHOICES

    return render(request, 'api_clinica/paciente/paciente_list.html', {
        'pacientes': pacientes,
        'query': query,
        'tipo_sangre_choices': tipo_sangre_choices,
        'selected_tipo_sangre': tipo_sangre_filter,
        'selected_activo': activo_filter,
    })

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente creado exitosamente!')
            return redirect('web_paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'api_clinica/paciente/paciente_form.html', {'form': form, 'action': 'Crear'})

def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado exitosamente!')
            return redirect('web_paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'api_clinica/paciente/paciente_form.html', {'form': form, 'action': 'Editar'})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado exitosamente!')
        return redirect('web_paciente_list')
    return render(request, 'api_clinica/paciente/paciente_confirm_delete.html', {'paciente': paciente})

# Vistas CRUD para Medico (sin cambios)
def medico_list(request):
    medicos = Medico.objects.all()
    query = request.GET.get('q')
    especialidad_filter = request.GET.get('especialidad')
    activo_filter = request.GET.get('activo')

    if query:
        medicos = medicos.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(rut__icontains=query) | Q(correo__icontains=query))

    if especialidad_filter:
        medicos = medicos.filter(especialidad__id=especialidad_filter)
    
    if activo_filter is not None:
        medicos = medicos.filter(activo=(activo_filter == 'true'))

    especialidades = Especialidad.objects.all()

    return render(request, 'api_clinica/medico/medico_list.html', {
        'medicos': medicos,
        'query': query,
        'especialidades': especialidades,
        'selected_especialidad': especialidad_filter,
        'selected_activo': activo_filter,
    })

def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico creado exitosamente!')
            return redirect('web_medico_list')
    else:
        form = MedicoForm()
    return render(request, 'api_clinica/medico/medico_form.html', {'form': form, 'action': 'Crear'})

def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico actualizado exitosamente!')
            return redirect('web_medico_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'api_clinica/medico/medico_form.html', {'form': form, 'action': 'Editar'})

def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        messages.success(request, 'Médico eliminado exitosamente!')
        return redirect('web_medico_list')
    return render(request, 'api_clinica/medico/medico_confirm_delete.html', {'medico': medico})

# Vistas CRUD para ConsultaMedica (sin cambios)
def consulta_medica_list(request):
    consultas = ConsultaMedica.objects.all()
    query = request.GET.get('q')
    paciente_filter = request.GET.get('paciente')
    medico_filter = request.GET.get('medico')
    estado_filter = request.GET.get('estado')

    if query:
        consultas = consultas.filter(Q(motivo__icontains=query) | Q(diagnostico__icontains=query))
    
    if paciente_filter:
        consultas = consultas.filter(paciente__id=paciente_filter)
    
    if medico_filter:
        consultas = consultas.filter(medico__id=medico_filter)

    if estado_filter:
        consultas = consultas.filter(estado=estado_filter)

    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    estados = ConsultaMedica.ESTADO_CHOICES

    return render(request, 'api_clinica/consulta_medica/consulta_medica_list.html', {
        'consultas': consultas,
        'query': query,
        'pacientes': pacientes,
        'medicos': medicos,
        'estados': estados,
        'selected_paciente': paciente_filter,
        'selected_medico': medico_filter,
        'selected_estado': estado_filter,
    })

def consulta_medica_create(request):
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta médica creada exitosamente!')
            return redirect('web_consulta_medica_list')
    else:
        form = ConsultaMedicaForm()
    return render(request, 'api_clinica/consulta_medica/consulta_medica_form.html', {'form': form, 'action': 'Crear'})

def consulta_medica_update(request, pk):
    consulta = get_object_or_404(ConsultaMedica, pk=pk)
    if request.method == 'POST':
        form = ConsultaMedicaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta médica actualizada exitosamente!')
            return redirect('web_consulta_medica_list')
    else:
        form = ConsultaMedicaForm(instance=consulta)
    return render(request, 'api_clinica/consulta_medica/consulta_medica_form.html', {'form': form, 'action': 'Editar'})

def consulta_medica_delete(request, pk):
    consulta = get_object_or_404(ConsultaMedica, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        messages.success(request, 'Consulta médica eliminada exitosamente!')
        return redirect('web_consulta_medica_list')
    return render(request, 'api_clinica/consulta_medica/consulta_medica_confirm_delete.html', {'consulta': consulta})

# Vistas CRUD para Tratamiento (sin cambios)
def tratamiento_list(request):
    tratamientos = Tratamiento.objects.all()
    query = request.GET.get('q')
    consulta_filter = request.GET.get('consulta')

    if query:
        tratamientos = tratamientos.filter(Q(descripcion__icontains=query) | Q(observaciones__icontains=query))
    
    if consulta_filter:
        tratamientos = tratamientos.filter(consulta__id=consulta_filter)

    consultas = ConsultaMedica.objects.all()

    return render(request, 'api_clinica/tratamiento/tratamiento_list.html', {
        'tratamientos': tratamientos,
        'query': query,
        'consultas': consultas,
        'selected_consulta': consulta_filter,
    })

def tratamiento_create(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tratamiento creado exitosamente!')
            return redirect('web_tratamiento_list')
    else:
        form = TratamientoForm()
    return render(request, 'api_clinica/tratamiento/tratamiento_form.html', {'form': form, 'action': 'Crear'})

def tratamiento_update(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tratamiento actualizado exitosamente!')
            return redirect('web_tratamiento_list')
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, 'api_clinica/tratamiento/tratamiento_form.html', {'form': form, 'action': 'Editar'})

def tratamiento_delete(request, pk):
    tratamiento = get_object_or_404(Tratamiento, pk=pk)
    if request.method == 'POST':
        tratamiento.delete()
        messages.success(request, 'Tratamiento eliminado exitosamente!')
        return redirect('web_tratamiento_list')
    return render(request, 'api_clinica/tratamiento/tratamiento_confirm_delete.html', {'tratamiento': tratamiento})

# Vistas CRUD para Medicamento (sin cambios)
def medicamento_list(request):
    medicamentos = Medicamento.objects.all()
    query = request.GET.get('q')
    laboratorio_filter = request.GET.get('laboratorio')

    if query:
        medicamentos = medicamentos.filter(Q(nombre__icontains=query) | Q(laboratorio__icontains=query))
    
    if laboratorio_filter:
        medicamentos = medicamentos.filter(laboratorio__icontains=laboratorio_filter)

    laboratorios_unicos = Medicamento.objects.order_by().values_list('laboratorio', flat=True).distinct()

    return render(request, 'api_clinica/medicamento/medicamento_list.html', {
        'medicamentos': medicamentos,
        'query': query,
        'laboratorios_unicos': laboratorios_unicos,
        'selected_laboratorio': laboratorio_filter,
    })

def medicamento_create(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento creado exitosamente!')
            return redirect('web_medicamento_list')
    else:
        form = MedicamentoForm()
    return render(request, 'api_clinica/medicamento/medicamento_form.html', {'form': form, 'action': 'Crear'})

def medicamento_update(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento actualizado exitosamente!')
            return redirect('web_medicamento_list')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'api_clinica/medicamento/medicamento_form.html', {'form': form, 'action': 'Editar'})

def medicamento_delete(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        messages.success(request, 'Medicamento eliminado exitosamente!')
        return redirect('web_medicamento_list')
    return render(request, 'api_clinica/medicamento/medicamento_confirm_delete.html', {'medicamento': medicamento})

# Vistas CRUD para RecetaMedica (sin cambios)
def receta_medica_list(request):
    recetas = RecetaMedica.objects.all()
    query = request.GET.get('q')
    tratamiento_filter = request.GET.get('tratamiento')
    medicamento_filter = request.GET.get('medicamento')

    if query:
        recetas = recetas.filter(Q(dosis__icontains=query) | Q(frecuencia__icontains=query) | Q(duracion__icontains=query))
    
    if tratamiento_filter:
        recetas = recetas.filter(tratamiento__id=tratamiento_filter)
    
    if medicamento_filter:
        recetas = recetas.filter(medicamento__id=medicamento_filter)

    tratamientos = Tratamiento.objects.all()
    medicamentos = Medicamento.objects.all()

    return render(request, 'api_clinica/receta_medica/receta_medica_list.html', {
        'recetas': recetas,
        'query': query,
        'tratamientos': tratamientos,
        'medicamentos': medicamentos,
        'selected_tratamiento': tratamiento_filter,
        'selected_medicamento': medicamento_filter,
    })

def receta_medica_create(request):
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta médica creada exitosamente!')
            return redirect('web_receta_medica_list')
    else:
        form = RecetaMedicaForm()
    return render(request, 'api_clinica/receta_medica/receta_medica_form.html', {'form': form, 'action': 'Crear'})

def receta_medica_update(request, pk):
    receta = get_object_or_404(RecetaMedica, pk=pk)
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta médica actualizada exitosamente!')
            return redirect('web_receta_medica_list')
    else:
        form = RecetaMedicaForm(instance=receta)
    return render(request, 'api_clinica/receta_medica/receta_medica_form.html', {'form': form, 'action': 'Editar'})

def receta_medica_delete(request, pk):
    receta = get_object_or_404(RecetaMedica, pk=pk)
    if request.method == 'POST':
        receta.delete()
        messages.success(request, 'Receta médica eliminada exitosamente!')
        return redirect('web_receta_medica_list')
    return render(request, 'api_clinica/receta_medica/receta_medica_confirm_delete.html', {'receta': receta})


# --- NUEVAS VISTAS CRUD PARA ENFERMERA (Basadas en Plantillas) ---
def enfermera_list(request):
    """
        Lista todas las enfermeras y permite buscar por nombre, apellido, RUT o correo.
        Permite filtrar por médico a cargo y estado activo.
    """
    enfermeras = Enfermera.objects.all()
    query = request.GET.get('q')
    medico_filter = request.GET.get('medico_a_cargo')
    activo_filter = request.GET.get('activo')

    if query:
        enfermeras = enfermeras.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(rut__icontains=query) | Q(correo__icontains=query))

    if medico_filter:
        enfermeras = enfermeras.filter(medico_a_cargo__id=medico_filter)
    
    if activo_filter is not None:
        enfermeras = enfermeras.filter(activo=(activo_filter == 'true'))

    medicos = Medico.objects.all() # Para el filtro en la plantilla

    return render(request, 'api_clinica/enfermera/enfermera_list.html', {
        'enfermeras': enfermeras,
        'query': query,
        'medicos': medicos,
        'selected_medico_a_cargo': medico_filter,
        'selected_activo': activo_filter,
    })

def enfermera_create(request):
    """
        Permite crear una nueva enfermera.
    """
    if request.method == 'POST':
        form = EnfermeraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enfermera creada exitosamente!')
            return redirect('web_enfermera_list')
    else:
        form = EnfermeraForm()
    return render(request, 'api_clinica/enfermera/enfermera_form.html', {'form': form, 'action': 'Crear'})

def enfermera_update(request, pk):
    """
        Permite editar una enfermera existente.
    """
    enfermera = get_object_or_404(Enfermera, pk=pk)
    if request.method == 'POST':
        form = EnfermeraForm(request.POST, instance=enfermera)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enfermera actualizada exitosamente!')
            return redirect('web_enfermera_list')
    else:
        form = EnfermeraForm(instance=enfermera)
    return render(request, 'api_clinica/enfermera/enfermera_form.html', {'form': form, 'action': 'Editar'})

def enfermera_delete(request, pk):
    """
        Elimina una enfermera.
    """
    enfermera = get_object_or_404(Enfermera, pk=pk)
    if request.method == 'POST':
        enfermera.delete()
        messages.success(request, 'Enfermera eliminada exitosamente!')
        return redirect('web_enfermera_list')
    return render(request, 'api_clinica/enfermera/enfermera_confirm_delete.html', {'enfermera': enfermera})
# -----------------------------------------------------------------------------

def inicio(request):
    return render(request, "api_clinica/home.html")