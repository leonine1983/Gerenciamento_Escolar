from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from gestao_escolar.models import Horario, TurmaDisciplina, Periodo, Turmas
from django import forms

class HorarioForm(ModelForm):
    segunda = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    terca = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quarta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quinta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    sexta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)

    class Meta:
        model = Horario
        fields = '__all__'
"""
def create_or_update_horario(request, turma_id, horario_id=None):
    # Obtém a turma com o ID fornecido
    turma = get_object_or_404(Turmas, pk=turma_id)
    
    # Verifica se já existe um horário para essa turma
    horario_turma = Horario.objects.filter(turma=turma)
    
    if horario_turma.exists():  # Se já existe um horário
        # Se o horário existe, atualize-o com os dados do formulário
        horario = horario_turma.first()  # Supondo que só haja um horário por turma
        form = HorarioForm(request.POST, instance=horario)  # Passe a instância existente para o formulário
        if form.is_valid():
            form.save()  # Salva as alterações no horário
    else:
        # Verifica se o horário já existe e obtém o objeto horário correspondente
        if horario_id:
            horario = get_object_or_404(Horario, pk=horario_id)
        else:
            horario = None

        if request.method == "POST":
            # Se for uma solicitação POST, verifica se o horário existe e cria um formulário com os dados recebidos
            form = HorarioForm(request.POST, instance=horario)
            print(f'contudo do form : {form}')
            if form.is_valid():
                # Salva o formulário e retorna para a página de criação de horário
                horario_instance = form.save(commit=False)
                horario_instance.turma = turma
                professor_conflito = None
                turma_conflito = None

                # Verifica conflito de professor nos dias da semana
                for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
                    turma_disciplina = getattr(horario_instance, dia)
                    if turma_disciplina:
                        conflito = Horario.objects.filter(
                            **{f'{dia}': turma_disciplina}
                        ).exclude(pk=horario_instance.pk).first()

                        if conflito:
                            professor_conflito = turma_disciplina.professor
                            turma_conflito = conflito.turma
                            break

                if professor_conflito:
                    messages.warning(
                        request,
                        f"O professor {professor_conflito} já está cadastrado na turma {turma_conflito} para o dia {dia}."
                    )
                else:
                    horario_instance.save()
                    messages.success(request, "Horário salvo com sucesso.")
                    return redirect('create_horario', turma_id=turma_id)
            else:
                # Se o formulário não for válido, exibe uma mensagem de erro
                messages.error(request, f"Erro ao salvar o formulário: {form.errors}")
        else:
            # Se for uma solicitação GET, cria um formulário com base no horário existente ou um novo objeto Horario
            form = HorarioForm(instance=horario)

    # Obtém todos os horários para a turma atual
    horarios = Horario.objects.filter(turma=turma)

    # Obtém todos os períodos disponíveis
    periodos = Periodo.objects.all()

    return render(request, 'Escola/inicio.html', {
        'turma_id': turma_id,
        'form': form,
        'horarios': horarios,
        'periodos': periodos,
        'conteudo_page': "Gestão Turmas - GerarHorario",
        'turma': turma
    })
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from gestao_escolar.models import Horario, TurmaDisciplina, Periodo, Turmas
from django import forms

class HorarioForm(forms.ModelForm):
    segunda = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    terca = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quarta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    quinta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)
    sexta = forms.ModelChoiceField(queryset=TurmaDisciplina.objects.all(), required=False)

    class Meta:
        model = Horario
        fields = '__all__'

def create_or_update_horario(request, turma_id, horario_id=None):
    # Obtém a turma com o ID fornecido
    turma = get_object_or_404(Turmas, pk=turma_id)
    
    # Verifica se já existe um horário para essa turma
    horario_turma = Horario.objects.filter(turma=turma)
    
    if horario_turma.exists():  # Se já existe um horário
        print (f'Esse é o post {request.POST}')
        # Se o horário existe, carrega as informações no formulário
        horario = horario_turma.first()  # Supondo que só haja um horário por turma
        form = HorarioForm(instance=horario)  # Passa a instância existente para o formulário
    else:
        horario = None
    
    if request.method == "POST":
        # Se for uma solicitação POST, verifica se o horário existe e cria um formulário com os dados recebidos
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            # Salva o formulário e retorna para a página de criação de horário
            horario_instance = form.save(commit=False)
            horario_instance.turma = turma
            # Restante do seu código aqui...
    else:
        # Se for uma solicitação GET, cria um formulário com base no horário existente ou um novo objeto Horario
        form = HorarioForm(instance=horario)

    # Obtém todos os horários para a turma atual
    horarios = Horario.objects.filter(turma=turma)

    # Obtém todos os períodos disponíveis
    periodos = Periodo.objects.all()

    return render(request, 'Escola/inicio.html', {
        'turma_id': turma_id,
        'form': form,
        'horarios': horarios,
        'periodos': periodos,
        'conteudo_page': "Gestão Turmas - GerarHorario",
        'turma': turma
    })
