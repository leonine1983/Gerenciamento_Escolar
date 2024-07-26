from django.db import models
from datetime import timedelta, date
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.core.exceptions import ValidationError

class Config_plataforma(models.Model):
    data = models.DateField(auto_now_add=True)
    rh_Ativo = models.BooleanField(default=False)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        if not Config_plataforma.objects.exists():
            Config_plataforma.objects.create(
                rh_Ativo = False
            )


class Uf_Unidade_Federativa(models.Model):
    sigla = models.CharField(max_length=2)
    estado = models.CharField(max_length=10)

    @receiver(post_migrate)
    def criar_registro(sender, *args, **kwargs):
        if not Uf_Unidade_Federativa.objects.exists():
            uf_estados = [
                ('AC', 'Acre'),
                ('AL', 'Alagoras'),
                ('AM', 'Amazonas'),
                ('AP', 'Amapá'),
                ('BA', 'Bahia'),
                ('CE', 'Ceará'),
                ('DF', 'Distrito Federal'),
                ('ES', 'Espírito Santos'),
                ('GO', 'Goiás'),
                ('MA', 'Maranhão'),
                ('MG', 'Minas Gerais'),
                ('MS', 'Mato Grosso do Sul'),
                ('MT', 'Mato Grosso'),
                ('PA', 'Pará'),
                ('PB', 'Paraíba'),
                ('PE', 'Pernambuco'),
                ('PI', 'Piauí'),
                ('PR', 'Paraná'),
                ('RJ', 'Rio de Janeiro'),
                ('RN', 'Rio Grande do Norte'),
                ('RO', 'Roraima'),
                ('RR', 'Rondônia'),
                ('RS', 'Rio Grande do Sul'),
                ('SC', 'Santa Catarina'),
                ('SE', 'Sergipe'),
                ('SP', 'São Paulo'),
                ('TO', 'Tocatins'),
            ]
            Uf_Unidade_Federativa.objects.bulk_create(
                [Uf_Unidade_Federativa(sigla = s, estado = e) for s, e in uf_estados]
            )

       

    def __str__(self):
        return f'{self.estado}/{self.sigla}'
    

class Prefeitura (models.Model):
    prefeitura_nome = models.CharField(max_length=50, null=False, default='Prefeitura')
    instituto = models.CharField(max_length=50, null=False, default='Nome da Instituição')
    cidade = models.CharField(max_length=30, null=False, default='')
    estado = models.ForeignKey(Uf_Unidade_Federativa, on_delete=models.CASCADE, null=True, blank=True)
    endereco = models.CharField(max_length=50, null=True, default='')
    pessoa_publica = models.CharField(max_length=30, null=False, default='')

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        if not Prefeitura.objects.exists():
            Prefeitura.objects.create(
                prefeitura_nome = 'Prefeitura Municipal de Algum Lugar',
                instituto = 'Secretaria Municipal da Educação',
                cidade = "Terra dos Sonhos",
                estado = Uf_Unidade_Federativa.objects.get(pk=1),
                endereco = 'Av. Te encontro lá',
                pessoa_publica = 'Petepan'
            )
   

    def __str__(self):
        return self.instituto


class Ano(models.Model):
    ano = models.CharField(max_length=4, null=False, verbose_name='Ano', default='2023')

    @receiver(post_migrate)
    def creat_register(sender, *args, **kwargs):
        if not Ano.objects.exists():
            Ano.objects.create(
                ano = '2023'
            )

    def __str__(self):
        return self.ano   


class Profissao(models.Model):
    nome_profissao = models.CharField(max_length=100, null=False, verbose_name='Profissão')
    descricao = models.TextField(max_length=500, null=False, verbose_name='Descreva a profissão')

    @receiver(post_migrate)
    def preenche_model(sender, **kwargs):

        nome_descreve =[
            ('Diretor Escolar', 'Profissional encarregado da administração e gestão de uma escola.'),
            ('Professor', 'Profissional dedicado à educação e ao ensino, desempenhando um papel fundamental na transmissão de conhecimentos, habilidades e valores para os alunos. Professores trabalham em diferentes níveis de ensino, desde a educação infantil até o ensino superior, em uma variedade de disciplinas e áreas de especialização.' ),
            ('Coordenador Escolar', 'Profissional que supervisiona as operações e as atividades educacionais de uma escola. Eles coordenam currículos, apoiam professores, lidam com questões disciplinares e interagem com pais e administração para garantir um ambiente de aprendizado eficaz e harmonioso, contribuindo para o funcionamento geral da instituição.'),
            ('Merendeira', 'Funcionária responsável pela preparação e distribuição das refeições escolares, garantindo uma alimentação saudável e adequada aos alunos. Elas mantêm a higiene da cozinha, seguem padrões nutricionais e contribuem para o bem-estar dos estudantes durante o dia escolar'),
            ('Técnica em alimentação escolar', 'Profissional especializada em planejar, preparar e supervisionar refeições nutritivas e balanceadas para alunos em ambiente escolar. '),
            ('Porteiro escolar','Profissional encarregado de monitorar e controlar o acesso à escola, garantindo a segurança dos alunos, funcionários e visitantes. Eles recebem e orientam pessoas que entram nas instalações, controlam a entrada e saída de alunos, ajudam a manter a ordem e auxiliam em situações de emergência, contribuindo para um ambiente escolar seguro e organizado.'),
            ('Secretária escolar', 'Profissional responsável por tarefas administrativas e organizacionais dentro de uma instituição de ensino. Elas lidam com matrículas, registros de alunos, comunicados, agendamento, documentação e atendimento aos pais e alunos.'),
            ( "Auxiliar Administrativo Escolar",'Profissional que oferece suporte em atividades administrativas dentro de uma instituição educacional. Suas responsabilidades podem incluir a organização de documentos, registros de alunos, atendimento telefônico, auxílio em tarefas contábeis e financeiras, agendamento e colaboração com a equipe administrativa para manter o funcionamento eficiente da escola.' )
        ]
        # Condição que verifica se existe registros no model Profissão, senão existir, ele roda o bulk_create
        if not Profissao.objects.exists():
            # o bulk_create cria várias instâncias de uma só vez, sendo mais eficiente que o objects.create que cria uma a uma
            Profissao.objects.bulk_create(
                [Profissao(nome_profissao = nome, descricao = descreve) for nome, descreve in nome_descreve]
            )                 
                    
         
    def __str__(self):
        return self.nome_profissao
    

class Salario(models.Model):
    ano = models.ForeignKey(Ano, null=True,verbose_name='Ano em que o valor do salário está vigente', on_delete=models.CASCADE)
    profissao = models.ForeignKey(Profissao, null=True, verbose_name='Profissão atendida pelo valor do salário', on_delete=models.CASCADE)
    cargaHoraria = models.IntegerField(null=True, verbose_name='Carga horária para o valor vigente')
    valor = models.CharField(max_length=100, null=True, verbose_name='Valor do salário')

    def __str__(self):
        return self.valor
    

class Sexo(models.Model):
    nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        sexos = ['Masculino', 'Feminino']
        if not Sexo.objects.exists():            
            Sexo.objects.bulk_create(
            [Sexo(nome = sexo) for sexo in sexos]
            )

    def __str__(self):
        return self.nome



class Pessoas(models.Model):
    nome = models.CharField(max_length=30, null=False, verbose_name='Nome')
    sobrenome = models.CharField(max_length=30, null=False, verbose_name='Sobrenome')    
    sexo = models.ForeignKey(Sexo, models.CASCADE, null=True)
    data_nascimento = models.DateField(null=True)    
    idade= models.CharField(max_length=9, null=True, blank=True)
    nome_profissao = models.ManyToManyField(Profissao, blank=True, verbose_name='Profissões')    
    cpf = models.CharField(max_length=30, null=True, verbose_name='CPF')
    rg= models.CharField(max_length=30, null=True, verbose_name='RG')
    rua= models.CharField(max_length=50, null=True, verbose_name='Nome da rua, avenida etc.')
    complemento= models.CharField(max_length=30, null=True, verbose_name='casa, apartamento etc.')
    numero_casa= models.CharField(max_length=10, null=True, verbose_name='Numero da casa ou s/n')
    bairro = models.CharField(max_length=30, null=True, verbose_name='Bairro')     
    cidade = models.CharField(max_length=30, null=True, verbose_name='Cidade')
    cep= models.CharField(max_length=30, null=True, verbose_name='CEP')   
    

    def calcula_idade (self):
        if self.data_nascimento:
            hoje = date.today()
            delta = hoje - self.data_nascimento
            anos = delta.days // 365
            return str(anos) + " anos"
        else:
            return None

        
    def save(self, *args, **kwargs):
        self.idade = self.calcula_idade()
        # Verificar se existe registros com as mesmas informações no BD,
        # se já tiver, ele impede o salvamento e emite uma mensagem
        existing_pessoas = Pessoas.objects.filter(
            nome = self.nome,
            cpf = self.cpf,
            rg = self.rg,            
        )
        if self.pk:
            existing_pessoas = existing_pessoas.exclude(pk = self.pk)
        # Se existir uma pessoa com as mesmas informações, gere um aviso
        if existing_pessoas.exists():
            raise ValidationError ("Já existe um registro com essas informações")
        super(Pessoas, self).save(*args, **kwargs)


    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'  


CHOICES = [
    ('professor', 'Professor'),
    ('funcionario', 'Funcionário'),
    ('estagio', 'Estágio'),
    ('voluntario', 'Voluntário')
]
class Texto_Contrato(models.Model):
    tipo = models.CharField(max_length=20, choices=CHOICES)
    # texto = RichTextField(blank=True, null=True)
    texto = models.TextField(max_length=2000, null=True, blank=True)
    


    def __str__(self):
        return self.tipo
    
class Escola(models.Model):
    prefeitura = models.ForeignKey(Prefeitura, on_delete=models.PROTECT, default='', verbose_name='Nome da Instituição Responsável')
    nome_escola = models.CharField(max_length=60, null=False, default='', verbose_name='Nome da Escola ou Departamento')
    endereco_escola = models.CharField(max_length=100, null=False, default='', verbose_name='Endereço')
    telefone_escola = models.CharField(max_length=30, null=True, default='', verbose_name='Telefone')
    # diretor
    # vice_diretor
    # coordenador1
    # coordenador1_turno
    # coordenador2
    # coordenador2_turno
    # coordenador3
    # coordenador3_turno
    # secretario

    @receiver(post_migrate)
    def cria_registro(sender, *args, **kwargs):
        escolas = [(Prefeitura.objects.all().first(), "Escola Teste 01", "Endereço 01", "(71) 9 86881943"),
                (Prefeitura.objects.all().first(), "Escola Teste 02", "Endereço 02", "(71) 9 86881943")]
        
        if not Escola.objects.exists():
            for prefeitura, nome, endereco, telefone in escolas:
                Escola.objects.create(
                    prefeitura=prefeitura,
                    nome_escola=nome,
                    endereco_escola=endereco,
                    telefone_escola=telefone
                )

    def __str__(self):
        return self.nome_escola

# Vinculo empregatício --------------------------------------------------------------------------
choice_vinculo = {
    ("contrato" , "Contrato"),
    ("decreto" , "Decreto"),
    ("efetivo" , "efetivo"),
    ("estagio" , "estagio"),
}

class Vinculo_empregaticio(models.Model):
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE, null=True)
    vinculo = models.CharField(max_length=10, choices=choice_vinculo, null=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.pessoa.nome



class Contrato(models.Model):
    ano_contrato = models.ForeignKey(Ano, related_name='ano_contrato_related',verbose_name='Ano do contrato', on_delete=models.CASCADE)
    contratado = models.ForeignKey(Pessoas, related_name='pessoa_contratada', verbose_name='Pessoa a ser contratada', on_delete=models.CASCADE)
    text_contrato = models.ForeignKey(Texto_Contrato,related_name='Texto_contrao_related', null=True, verbose_name='Vinculo com o tipo de contrato', on_delete=models.CASCADE)    
    nome_profissao = models.ForeignKey(Profissao, null=True, verbose_name='Função que irá desempenhar na escola', on_delete=models.CASCADE)     
    nome_escola = models.ForeignKey(Escola, null=True, verbose_name='Escola que o profissional irá desempenhar suas funções', on_delete=models.CASCADE) 
    salario = models.ForeignKey(Salario, null=True, verbose_name='Valor do salário para o cargo escolhido. Atente-se para o ano em que o valor do salário está vigente', on_delete=models.CASCADE)
    data_inicio_contrato = models.DateField(auto_now_add=True)
    data_fim_contrato = models.DateField(null=True)
    tempo_meses = models.IntegerField( null=True)

    def calcula_data_fim_contrato(self):
        if self.tempo_meses and self.data_inicio_contrato:
            # Se os campos tempo_mese e data_inicio_contrato for adicionado pelo usuario
            self.data_fim_contrato = self.data_inicio_contrato + timedelta(days=self.tempo_meses * 30)

    def save(self, *args, **kwargs):
        self.calcula_data_fim_contrato()
        super().save(*args, **kwargs)

    class Meta :
        ordering = ['ano_contrato']

    def __str__(self):
        return str(self.contratado)


    # Sobrescreve o método save para verifique se já existe algum registros com as informações fornecidas pelo usuario
    def save(self, *args, **kwargs):
        # Verifica se já existe um contrato com as mesmas informações
        existing_contracts = Contrato.objects.filter(
            contratado = self.contratado,
            nome_escola= self.nome_escola,
            ano_contrato = self.ano_contrato
        )

        # Exclua o contrato da atual consulta, se estiver atualizando
        if self.pk:
            existing_contracts = existing_contracts.exclude(pk=self.pk)
        # Se já existir um contrato com as mesmas informações, gere um aviso
        if existing_contracts.exists():
            raise ValidationError ("Já existe contrato com as mesmas informações")


        # Se não existir um contrato com as mesmas informações, continue salvando
        super().save(*args, **kwargs)






    
class Decreto(models.Model):
    profissional = models.ForeignKey(Pessoas, related_name='decreto_profissional', verbose_name='Profissional em que foi emitido o decreto', on_delete=models.CASCADE)
    destino = models.OneToOneField(Escola, related_name='local_decreto', null=False, verbose_name='Local onde o profissional será encaminhado', on_delete=models.CASCADE)
    profissao = models.ForeignKey(Profissao, null=False, verbose_name="Atividade a ser realizada pelo profissional", on_delete=models.CASCADE)
    ano_decreto = models.ForeignKey(Ano, on_delete=models.CASCADE, related_name='Ano_decreto', verbose_name="Ano do")
   

    def __str__(self):
        return self.profissional.nome


class Encaminhamentos(models.Model):
    encaminhamento = models.ForeignKey(Contrato, related_name='encaminhamento_escolar', verbose_name='Profissional a ser encaminhado', on_delete=models.CASCADE)
    destino = models.ForeignKey(Escola, related_name='local_encaminhamento', null=False, verbose_name='Local onde o profissional será encaminhado', on_delete=models.CASCADE)
    profissao = models.ForeignKey(Profissao, null=False, verbose_name="Atividade a ser realizada pelo profissional", on_delete=models.CASCADE)

    def __str__(self):
        return self.encaminhamento.contratado.nome  

    def save(self, *args, **kwargs):
        # Verifica se já existe um contrato com as mesmas informações
        existing_encaminhaments = Encaminhamentos.objects.filter(
            encaminhamento = self.encaminhamento,
            destino = self.destino,
            profissao = self.profissao            
        )

        # Exclua o contrato da atual consulta, se estiver atualizando
        if self.pk:
            existing_encaminhaments = existing_encaminhaments.exclude(pk = self.pk)
        # Se já existir um contrato com as mesmas informações, gere um aviso
        if existing_encaminhaments.exists():
            raise ValidationError ("Já existe contrato com as mesmas informações")


        # Se não existir um contrato com as mesmas informações, continue salvando
        super().save(*args, **kwargs)


class Frequencia_mes(models.Model):
    ano = models.ForeignKey(Ano, null=False, related_name='frequencia_ano', on_delete=models.CASCADE)
    mes = models.CharField(max_length=30, null=False, verbose_name='Mês')
    local = models.ForeignKey(Escola, related_name='local_frequencia', null=True, verbose_name='Local onde o profissional será encaminhado', on_delete=models.CASCADE)
    profissao = models.ForeignKey(Profissao, null=True,related_name='frequencia_profissional', verbose_name="Frequência do profissional", on_delete=models.CASCADE)

    def __str__(self):
        return self.mes
    