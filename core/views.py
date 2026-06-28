from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm, AtendimentoForm

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all().order_by('nome')
    return render(request, 'core/lista.html', {'pacientes': pacientes})

@login_required
def cadastrar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Cadastrar Novo Paciente'})

@login_required
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'core/formulario.html', {'form': form, 'titulo': 'Editar Dados do Paciente'})

@login_required
def excluir_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'core/excluir.html', {'paciente': paciente})

@login_required
def historico_atendimentos(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    atendimentos = paciente.atendimentos.all().order_by('-data_atendimento')
    
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        atendimento = form.save(commit=False)
        atendimento.paciente = paciente
        atendimento.save()
        return redirect('historico_atendimentos', paciente_id=paciente.id)
        
    return render(request, 'core/historico.html', {
        'paciente': paciente,
        'atendimentos': atendimentos,
        'form': form
    })