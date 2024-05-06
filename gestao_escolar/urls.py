from django.urls import path
from gestao_escolar.views.GE_pasta_escola import *
from gestao_escolar.views.pasta_session import *
from gestao_escolar.views import *
from gestao_escolar.views.views import   Pagina_inicio
from rh.models import Config_plataforma
#from dal import autocomplete
from .models import Alunos

app_name = "Gestao_Escolar"


urlpatterns = [
    path('gestao_escolar', ListView_Escola.as_view(), name="GE_inicio"),    
    path('escolas/selecionar/<int:pk>/', Seleciona_escola, name='escola-selecionar'),
    path('gestao_escolar/anoLetivo', Seleciona_anoLetivo.as_view(), name="GE_anoLetivo"),
    path('anoLetivo/selecionar/<int:pk>/', seleciona_anoLetivo_session, name='selecionar-ano'),
    # A parti daqui o desenvolvimento da escola inicia
    path('gestao_escolar/Escola/', Pagina_inicio.as_view(), name="GE_Escola_inicio"),
    

    # Turmas
    path('gestao_escolar/Turmas/', Create_turmas.as_view(), name="GE_Escola_turmas"),
    path('gestao_escolar/Turmas/all', ListView_Escola.as_view(), name="GE_Escola_turmas_lista"),
    path('gestao_escolar/Turmas/atualiza/<int:pk>', UpdateTurmas.as_view(), name="GE_Escola_Turmas_update"),    
    path('gestao_escolar/Turmas/delete/<int:pk>', Delete_Turmas.as_view(), name="GE_Escola_Turmas_delete"),

    # Alunos
    path('gestao_escolar/Alunos/', Create_Alunos.as_view(), name="GE_Escola_alunos_create"),
    path('gestao_escolar/Alunos/encontred/<str:nome_completo>/<str:nome_mae>', AlunosEcontred.as_view(), name="alunos_encontred"),
    path('gestao_escolar/Alunos/econtred', CreateAlunosConfirma.as_view(), name="alunos_create_encontred"),
    path('gestao_escolar/Alunos/etapa_2/<int:pk>', CreateAlunosConfirmaEtapa2.as_view(), name="alunos_create_etapa2"),


    path('gestao_escolar/Alunos/<int:pk>', Create_Alunos_Document.as_view(), name="GE_alunos_create_document"),    
    path('gestao_escolar/Alunos/documentos<int:pk>', Update_Alunos_Document.as_view(), name="GE_alunos_update_document"),
    path('gestao_escolar/Alunos/atualiza/<int:pk>', Update_Alunos.as_view(), name="GE_Escola_alunos_update"),    
    path('gestao_escolar/Alunos/delete/<int:pk>', Delete_Alunos.as_view(), name="GE_Escola_alunos_delete"),
    #path('autocomplete/', autocomplete.Select2ListView.as_view(), name='autocomplete_aluno'),
   

    # Matriculas
    path('gestao_escolar/Matricula/all_classes', View_turmas_Matriculas.as_view(), name="GE_Escola_Matricula_Turmas_lista"), 
    path('gestao_escolar/Matricula/create/<int:pk>', Create_Matriculas.as_view(), name="GE_Escola_Matricula_create"),      
    path('gestao_escolar/Matricula/all', List_Matriculas.as_view(), name="GE_Escola_Matricula_lista"),    

    # Matriculas retorno aluno
    path('gestao_escolar/Matricula/create/aluno/<int:pk>', Create_Matriculas_Retorno_alunos.as_view(), name="GE_Escola_Matricula_create_aluno"), 
   
    path('gestao_escolar/Matricula/atualiza/<int:pk>', Update_Matricula.as_view(), name="GE_Escola_Matricula_update"),    
    path('gestao_escolar/Matricula/delete/<int:pk>', Delete_Turmas.as_view(), name="GE_Escola_Matricula_delete"),

    # Remanejamento
    path('gestao_escolar/Matricula/remaneja_aluno/<int:pk>', Create_Remanejamento.as_view(), name="GE_Escola_Remaneja_create"),     
    path('gestao_escolar/Matricula/remaneja_aluno/Turma/<int:pk>', Update_Matricula_remanejamento.as_view(), name="GE_Escola_Remaneja_update"),     
    #path('gestao_escolar/Matricula/remaneja_aluno/Turma/<int:pk>', Update_Matricula_remanejamento.as_view(), name="GE_Escola_Remaneja_update"), 

    # Discplinas
    path('gestao_escolar/Disciplinas/create/', Create_disciplinas.as_view(), name="GE_Disciplina_create"),     
    path('gestao_escolar/Matricula/remaneja_aluno/Turma/<int:pk>', Update_Matricula_remanejamento.as_view(), name="GE_Escola_Remaneja_update"), 

    # Grades
    path('gestao_escolar/Grades/create/turmas', View_turmas_Grade.as_view(), name="Grades_turmas"),   
    path('gestao_escolar/Grades/create/<int:pk>', Create_Grades.as_view(), name="Grades_create"),     
    path('gestao_escolar/Matricula/remaneja_aluno/Turma/<int:pk>', Update_Matricula_remanejamento.as_view(), name="GE_Escola_Remaneja_update"), 

    # Professores
    path('gestao_escolar/Professores/Pessoas', Create_Pessoa_Professores.as_view(), name="Professores_Pessoa_create"),   
    path('gestao_escolar/Professores/Pessoas/vinculo/<int:pk>', Create_Pessoa_Vinculo.as_view(), name="Professores_Pessoa_vinculo_create"), 
    path('gestao_escolar/Professores/Pessoas/vinculo/aplica/<int:pk>,<slug:vinculo>,<int:ano>', Create_Pessoa_Aplica_Vinculo.as_view(), name="Professores_Pessoa_aplica_vinculo_create"),     
    path('gestao_escolar/Professores/Pessoas/encaminhamento/<int:pk>,<int:destino>,<int:profissao>', Create_Pessoa_Encaminhamento.as_view(), name="Professores_Encaminhamento"), 
    path('gestao_escolar/Professores/', Create_Professores.as_view(), name="GE_Professores_create"),     

    # Definir Profissionais
    path('gestao_escolar/Profissionais/', Create_Define_Profissional.as_view(), name="Professores_Profissionais_create"),  

    # Gestão de Turmas
    path('gestao_escolar/Gestao_Turmas/', Create_Notas.as_view(), name="NotasAluno_all_create"),  
    path('gestao_escolar/Gestao_Turmas/turma/<int:pk>', Create_Notas_pk.as_view(), name="NotasAluno_one_create"),  

    
    # IMPRESSOS
    path('turmas/impressao', Imprime_Turmas.as_view(), name='imprime_list_turmas'),


    # Ferramentas
    # path('image-to-doc/', Image_to_doc, name='image_to_doc'),

    # QR_code
    path('gestao_escolar/Criar_Qrcode/', Create_QrCode, name="GE_QrCode"),     
]

""" CRIA PROFESSORES - Aqui condiciona o acesso aos models pessoa, contrato e encaminhamento do app RH.
Caso o módulo RH não esteja ativo, o app Gestão_Escolar tem acesso à criação de registros de pessoas e seus segmentos.
"""
from django.db import connection

if Config_plataforma in connection.introspection.table_names():
    if Config_plataforma.objects.exists():
        config = Config_plataforma.objects.first()
        if config.rh_Ativo:
            urlpatterns.append(path('gestao_escolar/Pessoas/Criar/', Create_Pessoa_Professores.as_view(), name="GE_Create_Professores"))
        else:
            urlpatterns.append(path('gestao_escolar/Pessoas/Criar/', Create_Pessoa_Professores.as_view(), name="GE_Create_Professores"))
    else:
        urlpatterns.append(path('gestao_escolar/Pessoas/Criar/', Create_Pessoa_Professores.as_view(), name="GE_Create_Professores"))
else:
        urlpatterns.append(path('gestao_escolar/Pessoas/Criar/', Create_Pessoa_Professores.as_view(), name="GE_Create_Professores"))




