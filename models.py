from django.db import models
from django.db.models import CharField


class Estado(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'estado'

class Cidade(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cidade'


class Pais(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'pais'

class Funcao(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    codigo = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'funcao'


class Origem(models.Model):
    cidade = models.ForeignKey('Cidade', null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey('Estado', null=True, on_delete=models.SET_NULL)
    pais = models.ForeignKey('Pais', null=True, on_delete=models.SET_NULL)

    class Meta:

        db_table = 'origem'

class Destino(models.Model):
    cidade = models.ForeignKey('Cidade', null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey('Estado',null=True, on_delete=models.SET_NULL)
    pais = models.ForeignKey('Pais', null=True, on_delete=models.SET_NULL)

    class Meta:

        db_table = 'destino'


class FormaPagamento(models.Model):

    tipo = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'forma_pagamento'


class Cliente(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=60, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    cidade = models.ForeignKey('Cidade', null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey('Estado', null=True, on_delete=models.SET_NULL)
    data_cadastro = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


    class Meta:

        db_table = 'cliente'


class Documento(models.Model):
    nome_doc = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.nome_doc

    class Meta:

        db_table = 'documento'


class Empresa(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=80, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=80, blank=False, null=False)
    email = models.CharField(max_length=80, blank=False, null=False)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.ForeignKey('Cidade', null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey('Estado', null=True, on_delete=models.SET_NULL)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    data_inicio = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome



    class Meta:
        db_table = 'empresa'


class Fornecedor(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=80, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=80, blank=False, null=False)
    email = models.CharField(max_length=80, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    cidade = models.ForeignKey('Cidade', null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey('Estado', null=True, on_delete=models.SET_NULL)
    data_cadastro = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'fornecedor'


class Frota(models.Model):
    nome_frota = models.CharField(max_length=20, blank=False, null=False)
    empresa = models.ForeignKey('Empresa', null=True, on_delete=models.SET_NULL)
    situacoes = models.ForeignKey('Situacao', null=True, on_delete=models.SET_NULL)
    data_cadastro =models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_frota

    class Meta:
        db_table = 'frota'


class Exame(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    cid = models.CharField(max_length=40, blank=False, null=False)
   
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'exame'


class Funcionario(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cpf = models.CharField(db_column='CPF', max_length=50, blank=False, null=False)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30, blank=False, null=False)  # Field name made lowercase.
    data_admissao = models.DateField(null=False, blank=True)
    data_demissao = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=90, blank=False, null=False)
    funcao = models.ForeignKey('Funcao', null=True, on_delete=models.SET_NULL)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    cidade = models.ForeignKey('Cidade', null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey('Estado', null=True,on_delete=models.SET_NULL)
    situacoes = models.ForeignKey('situacao', null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'funcionario'


class LancarBaixaVeiculo(models.Model):
    veiculo = models.ForeignKey('veiculo', null=True, on_delete=models.SET_NULL)
    data_venda = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    comprador = models.CharField(max_length=60, blank=False, null=False)
    telefone_comprador = models.CharField(max_length=40, blank=False, null=False)


    class Meta:
        db_table = 'lancar_baixa_veiculo'


class LancarContabilidade(models.Model):
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    plano_conta = models.ForeignKey('PlanoConta', null=True, on_delete=models.SET_NULL)
    documento = models.ForeignKey('Documento', null=True, on_delete=models.SET_NULL)
    empresa = models.ForeignKey('Empresa', null=True, on_delete=models.SET_NULL)
    fornecedor = models.ForeignKey('Fornecedor',null=True, on_delete=models.SET_NULL)
    veiculo = models.ForeignKey('Veiculo', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'lancar_contabilidade'


class LancarFerias(models.Model):
    funcionario = models.ForeignKey('Funcionario', null=True, on_delete=models.SET_NULL)
    data_inicio = models.DateField(null=False, blank=True)
    data_fim = models.DateField(null=False, blank=True)
    ano_referente = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)


    class Meta:
        db_table = 'lancar_ferias'


class LancarFinanceiroViagem(models.Model):
    lancar_viagem = models.ForeignKey('LancarViagem', null=True, on_delete=models.SET_NULL)
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    plano_conta = models.ForeignKey('PlanoConta', null=True, on_delete=models.SET_NULL)
    documento = models.ForeignKey('Documento', null=True, on_delete=models.SET_NULL)
    empresa = models.ForeignKey('Empresa', null=True, on_delete=models.SET_NULL)
    fornecedor = models.ForeignKey('Fornecedor', null=True,on_delete=models.SET_NULL)
  

    class Meta:
        db_table = 'lancar_financeiro_viagem'


class LancarViagem(models.Model):
    crtc = models.CharField(max_length=30, blank=False, null=False)
    data = models.DateField(null=False, blank=True)
    frota = models.ForeignKey('Frota', null=True, on_delete=models.SET_NULL)
    motorista = models.ForeignKey('Funcionario', null=True, on_delete=models.SET_NULL)
    origem = models.ForeignKey('Origem', null=True, on_delete=models.SET_NULL)
    destino = models.ForeignKey('Destino', null=True, on_delete=models.SET_NULL)
    kminicial = models.IntegerField(db_column='kmInicial')  # Field name made lowercase.
    litragem = models.FloatField(null=False, blank=True)
    qtdeveiculos = models.IntegerField(null=False, blank=True)
    fk_empresa = models.ForeignKey('Empresa', null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.crtc


    class Meta:
        db_table = 'lancar_viagem'


class PlanoConta(models.Model):
    conta = models.IntegerField(null=False, blank=True)
    tipo = models.CharField(max_length=20, blank=False, null=False)
    descricao = models.CharField(max_length=20, blank=False, null=False)
    subconta = models.IntegerField(null=False, blank=True)
    sigla_situacao = models.CharField(max_length=1, blank=False, null=False)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.conta

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'plano_conta'


class Situacao(models.Model):
    tipo_nome = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_nome

    class Meta:
        db_table = 'situacao'


class TipoVeiculo(models.Model):
    tipo_veiculo = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.tipo_veiculo

    class Meta:
        db_table = 'tipo_veiculo'


class Veiculo(models.Model):
    tipo_veiculo = models.ForeignKey('TipoVeiculo', null=True, on_delete=models.SET_NULL)
    marca = models.CharField(max_length=80, blank=False, null=False)
    modelo = models.CharField(max_length=80, blank=False, null=False)
    ano = models.IntegerField(null=False, blank=True)
    data_fabricacao = models.DateField(null=False, blank=True)
    renavam = models.IntegerField(null=False, blank=True)
    placas = models.CharField(max_length=80, blank=False, null=False)
    datacompra = models.DateField('data', null=False, blank=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    empresa = models.ForeignKey('Empresa', null=True, on_delete=models.SET_NULL)
    frota = models.ForeignKey('Frota', null=True, on_delete=models.SET_NULL)
    tipo_aquisicao = models.CharField(max_length=50, blank=False, null=False)
    km_inicial = models.IntegerField(null=False, blank=True)
    situacoes = models.ForeignKey('situacao', null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)


    class Meta:
        db_table = 'veiculo'


class LancarDocVeiculo(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    data_realizado = models.DateField(null=False, blank=True)
    data_vencimento = models.DateField(null=False, blank=True)
    empresa = models.ForeignKey('Empresa', null=True, on_delete=models.SET_NULL)
    veiculo = models.ForeignKey('Veiculo', null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'lancar_doc_veiculo'


class AcertoViagem(models.Model):
    lancar_viagem = models.ForeignKey('LancarViagem', null=True, on_delete=models.SET_NULL)
    data_acerto = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    plano_conta = models.ForeignKey('PlanoConta', null=True, on_delete=models.SET_NULL)
    forma_pagamento = models.ForeignKey('FormaPagamento', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.data_acerto


    class Meta:

        db_table = 'acerto_viagem'

