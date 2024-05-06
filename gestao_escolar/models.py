from django.db import models
from django.utils import timezone
from decimal import Decimal

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from rh.models import Ano, Encaminhamentos, Escola, Profissao, Uf_Unidade_Federativa


class AnoLetivo(models.Model):
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    
    @receiver(post_migrate)
    def criar_registro(sender, *args, **kwargs):
        if not AnoLetivo.objects.exists():
            AnoLetivo.objects.create(
                ano = Ano.objects.get(id=1)
            )

    def __str__(self):
        return str(self.ano.ano)


class Cargo(models.Model):
    nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def create_register(sender, *args, **kwargs):
        cargos = [
                'Diretor',
                'Vice-Diretor',
                'Coordenador',
                'Professor',
                'Auxiliar-Administrativo-I',
                'Auxiliar-Administrativo-II',
                'Tecnico-em-Multimeitos-Didáticos',
                'Tecnico-em-Merenda-Escolar',
                'Auxiliar-de-Classe',
                'Servente-de-limpeza',
                'Monitor-de-Informática',                
                'Merendeira',
                'Porteiro',
                'Estagiário'
                 ]
        if not Cargo.objects.exists():            
            Cargo.objects.bulk_create(
                [Cargo(nome = n) for n in cargos]
            )

    def __str__(self):
        return self.nome  
    
    
class Etnia(models.Model):
    nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        etnias = ['Branca', 'Negra', 'Parda', 'Amarela', 'Indigena', 'Não declado']
        if not Etnia.objects.exists():            
            Etnia.objects.bulk_create(
            [Etnia(nome = etnia) for etnia in etnias]
            )

    def __str__(self):
        return self.nome
    

class Nacionalidade(models.Model):
    nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        nacionalidades = ['Brasileira', 'Brasileiro nascido no exterior', 'Mexicano']
        if not Nacionalidade.objects.exists():            
            Nacionalidade.objects.bulk_create(
            [Nacionalidade(nome = nacionalidade) for nacionalidade in nacionalidades]
            )

    def __str__(self):
        return self.nome
    

class Pais_origem(models.Model):
    nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        paises= ['Brasil', 'Japao', 'Mexico']
        if not Pais_origem.objects.exists():            
            Pais_origem.objects.bulk_create(
            [Pais_origem(nome = pais) for pais in paises]
            )

    def __str__(self):
        return self.nome
    

class Deficiencia_aluno(models.Model):
    nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        deficiencias= ['Física', 'Mental', 'Auditiva', 'Visual', 'Nenhuma']
        if not Deficiencia_aluno.objects.exists():            
            Deficiencia_aluno.objects.bulk_create(
            [Deficiencia_aluno(nome = deficiencia) for deficiencia in deficiencias]
            )

    def __str__(self):
        return self.nome
    
choices = {
    
    ('1','A+'),
    ('2','A-'),
    ('3','B+'),
    ('4','B-'),
    ('5','AB+'),
    ('6','AB-'),
    ('7','O+'),
    ('8','O-'),
    ('0','Não informado')
}

class Alunos(models.Model):
    nome_completo = models.CharField(max_length=120, null=False, default='Nome completo do aluno', verbose_name='Nome completo do aluno*')    
    nome_social = models.CharField(max_length=30, null=True, blank=True, default='')
    #sexo = models.ForeignKey(Sexo, on_delete= models.CASCADE, verbose_name='Gênero sexual do aluno*')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento*', null=True)    
    idade = models.IntegerField(null=True, blank=True)
    etnia = models.ForeignKey(Etnia, null=True, on_delete=models.CASCADE, verbose_name='Etnia do aluno*:')
    #aluno_inativo = models.BooleanField(default=False, null=True)
    tel_celular_aluno = models.CharField(max_length=30, null=False, default='Celular 01', verbose_name='Nº de telefone do aluno*')    
    email = models.EmailField(max_length=200, null=False, verbose_name='Email*')
    nome_mae = models.CharField(max_length=120, null=False, default='Nome completo da Mãe', verbose_name='Nome da Mãe*')
    tel_celular_mae = models.CharField(max_length=30, null=True, default='Telefone da mae', verbose_name='Nº do celular do mãe*')
    nome_pai = models.CharField(max_length=120, null=True, default='Nome completo da Pai')
    tel_celular_pai = models.CharField(max_length=30, null=True, default='Telefone do pai')
    naturalidade = models.CharField(max_length=30, null=False, default='Cidade onde nasceu')
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE, default=1, verbose_name='Nacionalidade*')
    pais_origem = models.ForeignKey(Pais_origem, blank=True, null=True, on_delete=models.CASCADE)
    data_entrada_no_pais= models.DateField(null=True, blank=True)  
    documento_estrangeiro = models.CharField(max_length=30, null=True, blank=True)
    deficiencia_aluno = models.ForeignKey(Deficiencia_aluno, on_delete=models.CASCADE, null=True, verbose_name='Informe se o aluno possui deficiência*')    
    tipo_sanguineo = models.CharField(max_length=3, choices=choices, null=True, )
    beneficiario_aux_Brasil = models.BooleanField(default=False,null=True, verbose_name='Selecione se o aluno é beneficiário do Bolsa Família/Aux. Brasil')
    necessita_edu_especial = models.BooleanField(default=False,null=True, verbose_name='Selecione se o aluno precisa de algum atendimento especial')
    sindrome_de_Down = models.BooleanField(default=False,null=True, verbose_name='Selecione se o aluno for portador de Síndrome de Down')
    quilombola = models.BooleanField(default=False,null=True, verbose_name='Selecione se o aluno possui deficiência')
    irmao_gemeo = models.BooleanField(default=False, null=True, verbose_name='Selecione se o aluno possui irmão(s) gêmeos')
    vacina_covid_19 = models.BooleanField(default=False, null=True,verbose_name='Selecione se o aluno tomou vacina contra a covid 19' )
    dose_vacina_covid_19 = models.IntegerField(null=True, blank=True, verbose_name='Preencha se o aluno tomou alguma dose da covid 19' )
    res_cadastro = models.CharField(max_length=120, null=True, default='Quem criou o cadastro')    
    res_atualiza_cadastro = models.CharField(max_length=120, null=True, default='Quem atualizou')    

    def __str__(self):
        return self.nome_completo 
    
choice_uf = {
    (1, 'AC'),
    (2, 'AL'),
    (3, 'AM'),
    (4, 'AP'),
    (5, 'BA'),
    (6, 'CE'),
    (7, 'DF'),
    (8, 'ES'),
    (9, 'GO'),
    (10, 'MA'),
    (11, 'MG'),
    (12, 'MS'),
    (13, 'MT'),
    (14, 'PA'),
    (15, 'PB'),
    (16, 'PE'),
    (17, 'PI'),
    (18, 'PR'),
    (19, 'RJ'),
    (20, 'RN'),
    (21, 'RO'),
    (22, 'RR'),
    (23, 'RS'),
    (24, 'SC'),
    (25, 'SE'),
    (26, 'SP'),
    (27, 'TO'),
}

choice_estado_civil = {
    ('1', 'Solteiro'),
    ('2', 'Casado'),
    ('3', 'Separado'),
    ('4', 'Divorciado'),
    ('5', 'Viúvo'),
    ('6', 'União Estável'),
}

choice_certidao = {
    ('1', 'Nascimento'),
    ('2', 'Casamento'),
    ('3', 'Outras')
}

choice_modelo_certidao = {
    ('1', 'Antigo'),
    ('2', 'Novo'),
    ('3', 'Nenhuma')
}

choice_justifica_falta_document= {
    ('1', 'o(a) aluno(a) não possui os documentos pessoais solicitados'),
    ('2', 'A escola não dispõe ou não recebeu os docum. pessoais do(a) aluno(a)')    
}

choice_local_diferenciado= {
    ('1', 'Não está em área de localização diferenciada'),
    ('2', 'Área de assentamento'),
    ('3', 'Terra indígena'),
    ('4', 'Área remanescente de quilombos'),    
    ('5', 'Área de povos e comunidades tradicionais'),  
}


class Alunos_Documentacao(models.Model):
    aluno = models.OneToOneField(Alunos, on_delete=models.CASCADE)
    RG = models.CharField(max_length=14, null=True, blank=True, default='000.000.00-00')    
    RG_emissao = models.DateField(null=True, blank=True, default=timezone.now)  
    RG_UF = models.OneToOneField(Uf_Unidade_Federativa, on_delete=models.CASCADE, null=True)
    orgao_emissor = models.CharField(max_length=5, null=True, blank=True)

    renda_familiar = models.CharField(max_length=7, null=True, blank=True)
    situacao_familiar = models.CharField(max_length=15, null=True, blank=True)

    CPF = models.CharField(max_length=14, null=True, blank=True, default='000.000.000-00')   

    login_aluno = models.CharField(max_length=10, null=True, blank=True)     
    senha = models.CharField(max_length=10, null=True, blank=True, default='12345678')
    
    cartao_nacional_saude_cns = models.CharField(max_length=20, null=True, blank=True)
    nis = models.CharField(max_length=20, null=True, blank=True)    
    inep = models.CharField(max_length=15, null=True, blank=True)
    estado_civil = models.CharField(max_length=13, null=True, blank=True, choices=choice_estado_civil) 
    tipo_certidao = models.CharField(max_length=13, null=True, blank=True, choices=choice_certidao) 
    numero_certidao = models.CharField(max_length=15, null=True, blank=True, verbose_name='Certidão de Nascimento (Matrícula Única)')
    livro = models.CharField(max_length=10, null=True, blank=True)
    folha = models.CharField(max_length=10, null=True, blank=True)
    termo = models.CharField(max_length=10, null=True, blank=True)
    emissao = models.DateField(null=True, blank=True)
    distrito_certidao= models.CharField(max_length=20, null=True, blank=True)
    cartorio = models.CharField(max_length=100, null=True, blank=True)
    comarca = models.CharField(max_length=100, null=True, blank=True)
    cartorio_uf = models.ForeignKey(Uf_Unidade_Federativa, related_name='relatio_cartorio_UF', null=True, on_delete=models.CASCADE)
    justificativa_falta_document = models.CharField(max_length=2, choices=choice_justifica_falta_document, null=True, blank=True, verbose_name='Justificativa da falta de documentação')
    local_diferenciado = models.CharField(max_length=2, choices=choice_justifica_falta_document, null=True, blank=True, verbose_name='Local Diferenciado')
    obito = models.BooleanField(null=True, blank=True,default=False)
    data_obito = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.aluno.nome_completo    

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ordem_historico = models.FloatField(null=True)
    n_A = models.BooleanField(verbose_name="Destacar como N/S (Não avaliado) nos impressos", default=False, null=True)
    #carga_horaria_anual = models.IntegerField()
    #categoria_grupo = pass
    faltas = models.BooleanField(verbose_name="Não permitir lançamento de faltas", default=False, null=True)
    notas = models.BooleanField(verbose_name="Não permitir lançamento de notas", default=False, null=True)
    historico_escolar = models.BooleanField(verbose_name="Não mostrar no histórico escolar", default=False, null=True)
    papeletas = models.BooleanField(verbose_name="Não mostrar em papeletas", default=False, null=True)
    ata_final = models.BooleanField(verbose_name="Não mostrar em Atas Finais", default=False, null=True)
    #educacacenso = models.Charfield(verbose_name="Integração com Educacenso")
    #unidade_curricular = models.Charfield(verbose_name="Unidade Curricular - Educacenso")

    @receiver(post_migrate)
    def create_register(sender, *args, **kwargs):
        disciplina = [
                ('Língua Portuguesa', 1),
                ('Língua Inglesa', 2),
                ('Matemática', 3),
                ('Ciências', 4),
                ('Geografia', 5),
                ('História', 6),
                ('Educação Ambiental', 7),
                ('Educação Artística', 8),
                ('Educação Física', 9), 
            ]
        if not Disciplina.objects.exists():
            Disciplina.objects.bulk_create(
                [Disciplina(nome = nomes, ordem_historico = histor) for nomes, histor in disciplina]
            )



    class Meta:
        ordering = ['ordem_historico']

    def __str__(self):
        return self.nome


class Compatibilidade_EducaCenso(models.Model):
    nome = models.CharField(max_length=100)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        areas = [
            'Ensino Fundamental de 9 anos - 1ºano',
            'Ensino Fundamental de 9 anos - 2ºano',
            'Ensino Fundamental de 9 anos - 3ºano',
            'Ensino Fundamental de 9 anos - 4ºano',
            'Ensino Fundamental de 9 anos - 5ºano',
            'Ensino Fundamental de 9 anos - 6ºano',
            'Ensino Fundamental de 9 anos - 7ºano',
            'Ensino Fundamental de 9 anos - 8ºano',
            'Ensino Fundamental de 9 anos - 9ºano',
            'EJA - Ensino Fundamental - Anos Iniciais',
            'EJA - Ensino Fundamental - Anos Finais',
            'Educação Infantil']

        if not Compatibilidade_EducaCenso.objects.exists():
            Compatibilidade_EducaCenso.objects.bulk_create(
                [Compatibilidade_EducaCenso(nome = area) for area in areas]
            )   

    def __str__(self):
        return self.nome

        
class GrauEscolar(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Grau/Nível Escolar" )

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        graus = ['Ensino Fundamental', 'Ensino Infantil']
        if not GrauEscolar.objects.exists():
            GrauEscolar.objects.bulk_create(
                [GrauEscolar(nome = grau) for grau in graus]
            )

    def __str__(self):
        return self.nome        


class Serie_Escolar(models.Model):
    nome = models.CharField(max_length=30)
    nivel_escolar = models.ForeignKey(GrauEscolar, null=False, on_delete=models.CASCADE)
    compatibilidade_EducaCenso = models.ForeignKey(Compatibilidade_EducaCenso, null=True, on_delete=models.CASCADE)
    # abreviacao = models.CharField(max_length=3, null=True)
    # carga_horaria = models.IntegerField(default=800)
    # compatibilidade_sed_sp = models.ForeignKey(Compatibilidade_sed_sp, null=False, on_delete=models.CASCADE)
    # nao_mostrar_no_historico_escola = models.BooleanField()
    # idade_ideal_creche_MIN = models.IntegerField()

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        series = [
            ('1º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=1)),
            ('2º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=2)),
            ('3º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=3)),
            ('4º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=4)),
            ('5º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=5)),
            ('6º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=6)),
            ('7º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=7)),
            ('8º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=8)),
            ('9º ano', GrauEscolar.objects.get(id=1), Compatibilidade_EducaCenso.objects.get(id=9)),
            ('G1', GrauEscolar.objects.get(id=2), Compatibilidade_EducaCenso.objects.get(id=1)),
            ('G1', GrauEscolar.objects.get(id=2), Compatibilidade_EducaCenso.objects.get(id=1)),
        ]
        if not Serie_Escolar.objects.exists():
            Serie_Escolar.objects.bulk_create(
                [Serie_Escolar (nome = serie, nivel_escolar = nivel, compatibilidade_EducaCenso = cenco ) for serie, nivel, cenco in series]
            )
        
    
    def __str__(self):
        return self.nome  

turno = {
    ('Matutino', 'Matutino'),
    ('Verspertino', 'Verspertino'),
    ('Noturno', 'Noturno')
}


class Turmas(models.Model):
    nome = models.CharField(max_length=10)
    descritivo_turma = models.CharField(max_length=10, default='única')
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE)
    serie =  models.ForeignKey(Serie_Escolar, on_delete=models.CASCADE)
    turno = models.CharField(choices=turno, null=False, default=1, max_length=12)    
    quantidade_vagas = models.CharField(max_length=2, default=36)
    turma_multiserie = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.nome

niveis = {
    ('1', "Médio"),
    ('2', "Superior")
}

# ---- Esta sessão inicia herdando do model Encaminhamentos do App RH.Models -------------------------------------
class Profissionais(models.Model):    
    nome = models.ForeignKey(Encaminhamentos, on_delete=models.CASCADE, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    area_especializacao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome.encaminhamento.contratado.nome
    

class Cursos(models.Model):
    nome = models.CharField(max_length=30)
    nivel = models.CharField(choices=niveis, max_length=1)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        if not Cursos.objects.exists():
            Cursos.objects.create(
                nome = "Licenciatura em Pedagogia",
                nivel = 2
            )


class Faculdades_ou_Escolas (models.Model):
    nome = models.CharField(max_length=50)   

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        if not Faculdades_ou_Escolas.objects.exists():
            Faculdades_ou_Escolas.objects.create(
                nome = "UNEB - Universidade Estadual da Bahia",                
            ) 
    

"""
# A class Professores descende da class Profissionais 
class Professores(models.Model):  # Não inclua um campo 'id' aqui
    docente = models.ForeignKey(Profissionais, on_delete=models.CASCADE, null=True)
    escolas = models.ManyToManyField(Escola)
    data_entrada_escola = models.DateField(null=False)
    data_saida_escola = models.DateField(null=True)
    efetivo = models.BooleanField(default=False)
    # ---------------------------------------------
    disciplina = models.ManyToManyField(Disciplina)
    formacao_academica = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True)
    instituto_academico = models.ForeignKey(Faculdades_ou_Escolas, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(null=True)


# Professores auxiliares 
"""


class TurmaDisciplina(models.Model):
    turma = models.ForeignKey(Turmas, on_delete=models.CASCADE, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)
    professor = models.ForeignKey(Profissionais, on_delete=models.CASCADE, null=True)
    carga_horaria_anual = models.IntegerField(null=True)
    limite_faltas = models.IntegerField(null=True) 

    def __str__(self):
        return self.disciplina.nome

   
escola_fora = {
    ('1','Não recebe'), 
    ('2','Em hospital'),
    ('3', 'Em domicílio')
}

class Matriculas(models.Model):
    aluno = models.ForeignKey(Alunos, related_name='related_matricula_alunos', on_delete=models.CASCADE)
    turma = models.ForeignKey(Turmas, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now=True)
    obervacao = models.TextField(max_length=300, null=True, blank=True)
    escolarizacao_fora = models.CharField(choices=escola_fora, default=1, max_length=1)
    serie_multiseriada  = models.ForeignKey(Serie_Escolar, null=True, blank=True, on_delete=models.CASCADE)
    #periodo_multiserie = models.CharField(choices=turno, null=True, max_length=12 )
    data_afastamento_inicio = models.DateField(null=True)
    data_afastamento_fim = models.DateField(null=True)
    motivo_afastamento = models.TextField(max_length=200, null=True)
    calcula_media = models.BooleanField(default=True)

    """
    # Sobrescrever o método save para verificar se o aluno ja está matriculado em alguma turma
    def save(self, *args, **kwargs):
        # Verifica se o aluno está matriculado em alguma turma, de qualquer escola do aluno letivo atual
        matricula_exist = Matriculas.objects.filter(aluno = self.aluno, turma__ano_letivo = self.request.session['anoLetivo_id'])
        
        # Se tiver atualizando, exclua a matricula atual
        if self.pk:
            matricula_exist = matricula_exist.exclude(pk = self.pk)
        # Se já existir uma matricula do aluno no ano letivo atual, gere um aviso
        if matricula_exist.exists():
            matricula = Matriculas.objects.filter(pk = self.pk)
            for n in matricula:
                matricula_turma = n.turma.nome
                matricula_escola = n.turma.escola
                matricula_ano = n.turma.ano_letivo

            raise ValueError (f"O aluno ja está matriculado na turma do {matricula_turma}, da escola {matricula_escola} no Ano Letivo {matricula_ano}  ")
        super().save(*args, **kwargs)
 
        
    
    """
    
    

    def __str__(self):
        return self.aluno.nome_completo

remaneja_tipo = {
    ('Ativo', 'Na Turma'),
    ('Desistente', 'Desistente/Evasão Escolar'),
    ('Transferido', 'Noturno')
}

class Remanejamento(models.Model):    
    tipo = models.CharField(max_length=26, choices=remaneja_tipo, default='Ativo', null=False, verbose_name="Tipo de remanejamento")
    description = models.TextField(max_length=500, verbose_name="Descreva o motivo do Remanejamento. Ex.: Escola para onde o aluno será remanejado e o porquê.", )
    data = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.tipo



# ------------------------------------------------------------------------------------
# ------------------------- Atividades do aluno --------------------------------------
# ------------------------------------------------------------------------------------

class Trimestre(models.Model):
    numero_nome = models.CharField(null=True, max_length=14)
    ano_letivo = models.ForeignKey(AnoLetivo, null=True, on_delete=models.CASCADE)
    # soma_notas = models.BooleanField(default=True)  # Se True, a nota será a soma das pontuações; se False, será a média

    @receiver(post_migrate)
    def create_registre(sender, *args, **kwargs):
        trimestre = [('I Trimestre', AnoLetivo.objects.get(id=1)),
                     ('II Trimestre', AnoLetivo.objects.get(id=1)),
                     ('III Trimestre', AnoLetivo.objects.get(id=1))]
        if not Trimestre.objects.exists():
            Trimestre.objects.bulk_create(
                [Trimestre(numero_nome = num, ano_letivo = ano) for num, ano in trimestre]
            )


    def __str__(self):
        return self.numero_nome
    

class Trimestral_Notas_Aluno(models.Model):
    grade = models.ForeignKey(TurmaDisciplina, null=True, on_delete=models.CASCADE)
    trimestre = models.ForeignKey(Trimestre, null=True, on_delete=models.CASCADE)
    aluno_matriculados = models.ForeignKey(Matriculas, null=True, on_delete=models.CASCADE)    
    notas = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Notas do {self.trimestre.numero_nome} do aluno {self.aluno_matriculados.aluno.nome_completo}'
    

"""
class Atividade(models.Model):
    disciplina = models.ForeignKey(Disciplina, null=True, on_delete=models.CASCADE)
    avaliativa = models.BooleanField( null=True)
    pontuacao = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    alunos = models.ManyToManyField(Alunos,null=True, through='AtividadeAluno')

    def __str__(self):
        return f'Disciplina: {self.disciplina} - Avaliativa: {self.avaliativa}'
    


class PerguntasAbertas(models.Model):
    atividade = models.ForeignKey(Atividade,null=True, on_delete=models.CASCADE)
    pergunta = models.TextField(null=True)
    resposta = models.TextField(null=True)

    def __str__(self):
        return f'Atividade: {self.atividade} - Pergunta: {self.pergunta}'


class PerguntasMultiplaEscolha(models.Model):
    atividade = models.ForeignKey(Atividade,null=True, on_delete=models.CASCADE)
    pergunta = models.TextField(null=True)

    def __str__(self):
        return f'Atividade: {self.atividade} - Pergunta: {self.pergunta}'


class OpcaoMultiplaEscolha(models.Model):
    pergunta = models.ForeignKey(PerguntasMultiplaEscolha,null=True, on_delete=models.CASCADE)
    opcao = models.CharField(null=True, max_length=200)
    correta = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f'Pergunta: {self.pergunta} - Opção: {self.opcao}'


class PerguntaObjetiva(models.Model):
    atividade = models.ForeignKey(Atividade,null=True, on_delete=models.CASCADE)
    pergunta = models.TextField(null=True)

    def __str__(self):
        return f'Atividade: {self.atividade} - Pergunta: {self.pergunta}'


class AtividadeReutilizada(models.Model):
    atividade = models.ForeignKey(Atividade,null=True, on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey(AnoLetivo,null=True, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turmas,null=True, on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola,null=True, on_delete=models.CASCADE)

    def __str__(self):        
        return f'Atividade: {self.atividade} - Turma: {self.turma} - Escola: {self.escola}'



class Notas(models.Model):
    aluno = models.ForeignKey(Alunos,null=True, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade,null=True, on_delete=models.CASCADE)
    acertos = models.IntegerField()

    def __str__(self):
        return f'Aluno: {self.aluno} - Atividade: {self.atividade}'

class AtividadeAluno(models.Model):    
    trimestre = models.ForeignKey(Trimestre,null=True, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade,null=True, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Alunos,null=True, on_delete=models.CASCADE)
    professor = models.ForeignKey(Profissionais,null=True, on_delete=models.CASCADE)
    acertos = models.IntegerField(null=True)

    def __str__(self):
        return f'Atividade: {self.atividade} - Aluno: {self.aluno}'


"""  