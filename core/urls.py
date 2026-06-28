from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Rotas de Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Rotas do Sistema
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('paciente/novo/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('paciente/<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('paciente/<int:pk>/excluir/', views.excluir_paciente, name='excluir_paciente'),
    path('paciente/<int:paciente_id>/historico/', views.historico_atendimentos, name='historico_atendimentos'),
]