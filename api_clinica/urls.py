# api_clinica/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs para las vistas de la API (DRF)
    path('especialidades/', views.EspecialidadListCreate.as_view(), name='especialidad-list-create'), # Listar y crear especialidades
    path('especialidades/<int:pk>/', views.EspecialidadRetrieveUpdateDestroy.as_view(), name='especialidad-detail'), # Ver, actualizar y eliminar especialidad

    path('medicos/', views.MedicoListCreate.as_view(), name='medico-list-create'), # Listar y crear médicos
    path('medicos/<int:pk>/', views.MedicoRetrieveUpdateDestroy.as_view(), name='medico-detail'), # Ver, actualizar y eliminar médico

    path('pacientes/', views.PacienteListCreate.as_view(), name='paciente-list-create'), # Listar y crear pacientes
    path('pacientes/<int:pk>/', views.PacienteRetrieveUpdateDestroy.as_view(), name='paciente-detail'), # Ver, actualizar y eliminar paciente

    path('consultas/', views.ConsultaMedicaListCreate.as_view(), name='consultamedica-list-create'), # Listar y crear consultas médicas
    path('consultas/<int:pk>/', views.ConsultaMedicaRetrieveUpdateDestroy.as_view(), name='consultamedica-detail'), # Ver, actualizar y eliminar consulta médica

    path('tratamientos/', views.TratamientoListCreate.as_view(), name='tratamiento-list-create'), # Listar y crear tratamientos
    path('tratamientos/<int:pk>/', views.TratamientoRetrieveUpdateDestroy.as_view(), name='tratamiento-detail'), # Ver, actualizar y eliminar tratamiento

    path('medicamentos/', views.MedicamentoListCreate.as_view(), name='medicamento-list-create'), # Listar y crear medicamentos
    path('medicamentos/<int:pk>/', views.MedicamentoRetrieveUpdateDestroy.as_view(), name='medicamento-detail'), # Ver, actualizar y eliminar medicamento

    path('recetas/', views.RecetaMedicaListCreate.as_view(), name='recetamedica-list-create'), # Listar y crear recetas médicas
    path('recetas/<int:pk>/', views.RecetaMedicaRetrieveUpdateDestroy.as_view(), name='recetamedica-detail'), # Ver, actualizar y eliminar receta médica

    path('enfermeras/', views.EnfermeraListCreate.as_view(), name='enfermera-list-create'), # Listar y crear enfermeras
    path('enfermeras/<int:pk>/', views.EnfermeraRetrieveUpdateDestroy.as_view(), name='enfermera-detail'), # Ver, actualizar y eliminar enfermera

    # URLs para las vistas basadas en plantillas (HTML, CSS, Bootstrap) - CRUD completo
    path('web/especialidades/', views.especialidad_list, name='web_especialidad_list'), # Listar especialidades
    path('web/especialidades/crear/', views.especialidad_create, name='web_especialidad_create'), # Crear especialidad
    path('web/especialidades/editar/<int:pk>/', views.especialidad_update, name='web_especialidad_update'), # Editar especialidad
    path('web/especialidades/eliminar/<int:pk>/', views.especialidad_delete, name='web_especialidad_delete'), # Eliminar especialidad

    path('web/pacientes/', views.paciente_list, name='web_paciente_list'), # Listar pacientes
    path('web/pacientes/crear/', views.paciente_create, name='web_paciente_create'), # Crear paciente
    path('web/pacientes/editar/<int:pk>/', views.paciente_update, name='web_paciente_update'), # Editar paciente
    path('web/pacientes/eliminar/<int:pk>/', views.paciente_delete, name='web_paciente_delete'), # Eliminar paciente

    path('web/medicos/', views.medico_list, name='web_medico_list'), # Listar médicos
    path('web/medicos/crear/', views.medico_create, name='web_medico_create'), # Crear médico
    path('web/medicos/editar/<int:pk>/', views.medico_update, name='web_medico_update'), # Editar médico
    path('web/medicos/eliminar/<int:pk>/', views.medico_delete, name='web_medico_delete'), # Eliminar médico

    path('web/consultas/', views.consulta_medica_list, name='web_consulta_medica_list'), # Listar consultas médicas
    path('web/consultas/crear/', views.consulta_medica_create, name='web_consulta_medica_create'), # Crear consulta médica
    path('web/consultas/editar/<int:pk>/', views.consulta_medica_update, name='web_consulta_medica_update'), # Editar consulta médica
    path('web/consultas/eliminar/<int:pk>/', views.consulta_medica_delete, name='web_consulta_medica_delete'), # Eliminar consulta médica

    path('web/tratamientos/', views.tratamiento_list, name='web_tratamiento_list'), # Listar tratamientos
    path('web/tratamientos/crear/', views.tratamiento_create, name='web_tratamiento_create'), # Crear tratamiento
    path('web/tratamientos/editar/<int:pk>/', views.tratamiento_update, name='web_tratamiento_update'), # Editar tratamiento
    path('web/tratamientos/eliminar/<int:pk>/', views.tratamiento_delete, name='web_tratamiento_delete'), # Eliminar tratamiento

    path('web/medicamentos/', views.medicamento_list, name='web_medicamento_list'), # Listar medicamentos
    path('web/medicamentos/crear/', views.medicamento_create, name='web_medicamento_create'), # Crear medicamento
    path('web/medicamentos/editar/<int:pk>/', views.medicamento_update, name='web_medicamento_update'), # Editar medicamento
    path('web/medicamentos/eliminar/<int:pk>/', views.medicamento_delete, name='web_medicamento_delete'), # Eliminar medicamento

    path('web/recetas/', views.receta_medica_list, name='web_receta_medica_list'), # Listar recetas médicas
    path('web/recetas/crear/', views.receta_medica_create, name='web_receta_medica_create'), # Crear receta médica
    path('web/recetas/editar/<int:pk>/', views.receta_medica_update, name='web_receta_medica_update'), # Editar receta médica
    path('web/recetas/eliminar/<int:pk>/', views.receta_medica_delete, name='web_receta_medica_delete'), # Eliminar receta médica

    path('web/enfermeras/', views.enfermera_list, name='web_enfermera_list'), # Listar enfermeras
    path('web/enfermeras/crear/', views.enfermera_create, name='web_enfermera_create'), # Crear enfermera
    path('web/enfermeras/editar/<int:pk>/', views.enfermera_update, name='web_enfermera_update'), # Editar enfermera
    path('web/enfermeras/eliminar/<int:pk>/', views.enfermera_delete, name='web_enfermera_delete'), # Eliminar enfermera


    # URL para la página de inicio (dashboard o página principal)
    path('', views.home, name='home'),
]