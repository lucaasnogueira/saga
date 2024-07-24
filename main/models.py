from django.db import models
from django.utils import timezone
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Transportadora(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Transforma o nome para maiúsculas antes de salvar
        self.nome = self.nome.upper()
        
        # Formata o CNPJ com pontos e traços (se não estiver já formatado)
        if self.cnpj and '.' not in self.cnpj and '-' not in self.cnpj:
            self.cnpj = '{}.{}.{}/{}-{}'.format(
                self.cnpj[:2], self.cnpj[2:5], self.cnpj[5:8], self.cnpj[8:12], self.cnpj[12:14]
            )
        
        super().save(*args, **kwargs)


class Motorista(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    cpf = models.CharField(max_length=14, unique=True)  
    empresa = models.ForeignKey(Transportadora, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Transforma o nome para maiúsculas antes de salvar
        self.nome = self.nome.upper()
        
        # Formata o CPF com pontos (se não estiver já formatado)
        if self.cpf and '-' not in self.cpf:
            self.cpf = '{}.{}.{}-{}'.format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])
        
        super().save(*args, **kwargs)

class Porto(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome.upper()
    

class Conferente(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=5)

    def __str__(self):
        return self.nome.upper()
    

class TipoContainer(models.Model):
    tipo = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.tipo
    

class Preenchimento(models.Model):
    tipo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.tipo
    

class Localização(models.Model):
    localização = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.localização


class Lacre(models.Model):
    numero = models.CharField(max_length=6, unique=True)
    
    def __str__(self):
        return self.numero



class AvariaCarga(models.Model):
    avaria = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.avaria.upper()


class TipoAvaria(models.Model):
    avaria = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.avaria
    


class Cliente(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        
        # Formata o CNPJ com pontos e traços (se não estiver já formatado)
        if self.cnpj and '.' not in self.cnpj and '-' not in self.cnpj:
            self.cnpj = '{}.{}.{}/{}-{}'.format(
                self.cnpj[:2], self.cnpj[2:5], self.cnpj[5:8], self.cnpj[8:12], self.cnpj[12:14]
            )
        
        super().save(*args, **kwargs)    
    

def validate_numero_container(value):
    if not re.match(r'^[A-Z]{3}\d{4}$', value):
        raise ValidationError('O número da placa deve seguir o padrão AAA1234.')

class Container(models.Model):
    numero = models.CharField(max_length=12)
    data_entrada = models.DateTimeField(auto_now=False, )
    data_saida = models.DateTimeField(auto_now=False, null=True, blank=True)
    demurrage = models.DateField(auto_now=False, null=True)
    preenchimento = models.ForeignKey(Preenchimento, on_delete=models.PROTECT)
    cavalo_entrada = models.CharField(max_length=8)
    cavalo_saida = models.CharField(max_length=8, blank=True, null=True)
    prancha_entrada = models.CharField(max_length=8)
    prancha_saida = models.CharField(max_length=8, blank=True, null=True)
    motorista_Entrada = models.ForeignKey(Motorista, on_delete=models.PROTECT, related_name='motorista_entrada_set', blank=True)
    motorista_Saida = models.ForeignKey(Motorista, on_delete=models.PROTECT, related_name='motorista_saida_set', blank=True, null=True)
    lacre = models.CharField(max_length=10, unique=True)
    porto = models.ForeignKey(Porto, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoContainer, on_delete=models.PROTECT)
    origem = models.CharField(max_length=25)
    destino = models.CharField(max_length=25, blank=True)
    transportador = models.ForeignKey(Transportadora, on_delete=models.PROTECT)
    localização = models.ForeignKey(Localização,null=True, blank=True, on_delete=models.PROTECT)
    avaria = models.ManyToManyField(TipoAvaria, blank=True, null=True)

    def __str__(self):
        return self.numero
    
    def clean(self):
        super().clean()
        self.numero = self.clean_numero(self.numero)

    @staticmethod
    def clean_numero(numero):
        # Remove espaços em branco extras e converte para maiúsculas
        numero = numero.strip().upper()

        # Verifica se o número do contêiner segue o padrão ISO 6346
        pattern = re.compile(r'^[A-Z]{4}\d{7}$')
        if not pattern.match(numero):
            raise ValidationError(('Número do contêiner deve seguir o padrão ISO 6346: quatro letras seguidas de sete dígitos.'))

        return numero

    def save(self, *args, **kwargs):
        self.full_clean()  # Validação completa antes de salvar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero
    
    

class Container_Aurora(models.Model):
    numero = models.CharField(max_length=11)
    data_inicio = models.DateField(auto_now=False, null=True)
    data_fim = models.DateField(auto_now=False, null=True, blank=True)
    fornecedor = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.numero
    
    def clean(self):
        super().clean()
        self.numero = self.clean_numero(self.numero)

    @staticmethod
    def clean_numero(numero):
        # Remove espaços em branco extras e converte para maiúsculas
        numero = numero.strip().upper()

        # Verifica se o número do contêiner segue o padrão ISO 6346
        pattern = re.compile(r'^[A-Z]{4}\d{7}$')
        if not pattern.match(numero):
            raise ValidationError(('Número do contêiner deve seguir o padrão ISO 6346: quatro letras seguidas de sete dígitos.'))

        return numero

    def save(self, *args, **kwargs):
        self.full_clean()  # Validação completa antes de salvar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero


class Carga(models.Model):
    numero_Nota_Fiscal = models.CharField(max_length=20)
    data_Lançamento_NF = models.DateTimeField(auto_now=False, blank=True, null=True)
    numero_DI = models.CharField(max_length=30, blank=True, null=True)
    data_entrada = models.DateTimeField(auto_now=False)
    data_saida = models.DateTimeField(auto_now=False, null=True, blank=True)
    container_entrada = models.ForeignKey(Container, on_delete=models.PROTECT, related_name='carga_entrada_set')
    container_saida = models.ForeignKey(Container, on_delete=models.PROTECT, related_name='carga_saida_set', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.PROTECT)
    quantidade_de_caixas_ou_volume = models.CharField(max_length=5)
    avaria = models.ManyToManyField(AvariaCarga, blank=True, null=True)

    def __str__(self):
        return self.numero_Nota_Fiscal
    

class Desunitição_e_Unitização(models.Model):
    carga = models.ForeignKey(Carga, on_delete=models.PROTECT)
    container_Origem = models.ForeignKey(Container, on_delete=models.PROTECT)
    container_Cedido = models.ForeignKey(Container_Aurora, on_delete=models.PROTECT)
    quantidade_de_caixas_ou_volume = models.CharField(max_length=5)
    lacre_Original = models.CharField(max_length=10, unique=True)
    lacre_Aurora = models.ForeignKey(Lacre, on_delete=models.PROTECT)
    data_Deslacre = models.DateTimeField(auto_now=False)
    data_inicio = models.DateTimeField(auto_now=False)
    data_fim = models.DateTimeField(auto_now=False, blank=True)
    conferente = models.ForeignKey(Conferente, on_delete=models.PROTECT)

    def __str__(self):
        return f'Carga #{self.id}'
    
    @staticmethod
    def get_desunitizacoes_count():
        return Desunitição_e_Unitização.objects.count()


class Cedido(models.Model):
    numero = models.ForeignKey(Container_Aurora, on_delete=models.PROTECT)
    data_saida = models.DateTimeField(null=True, blank=True)
    data_retorno = models.DateTimeField(null=True, blank=True)
    preenchimento_saida = models.ForeignKey(Preenchimento, on_delete=models.PROTECT, related_name='cedido_preenchimento_saida', blank=True)
    preenchimento_retorno = models.ForeignKey(Preenchimento, on_delete=models.PROTECT, related_name='cedido_preenchimento_retorno', blank=True, null=True)
    cavalo_saida = models.CharField(max_length=8)
    cavalo_retorno = models.CharField(max_length=8, blank=True, null=True)
    prancha_saida = models.CharField(max_length=8)
    prancha_retorno = models.CharField(max_length=8, blank=True, null=True)
    motorista_saida = models.ForeignKey(Motorista, on_delete=models.PROTECT, related_name='cedido_motorista_saida', blank=True)
    motorista_retorno = models.ForeignKey(Motorista, on_delete=models.PROTECT, related_name='cedido_motorista_retorno', blank=True, null=True)
    lacre = models.ForeignKey(Lacre, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoContainer, on_delete=models.PROTECT)
    origem = models.CharField(max_length=25)
    destino = models.CharField(max_length=25, blank=True)
    transportador = models.ForeignKey(Transportadora, on_delete=models.PROTECT)
    avaria = models.ManyToManyField(TipoAvaria, blank=True)

    def __str__(self):
        return self.numero
    
    def clean(self):
        super().clean()
        self.numero = self.clean_numero(self.numero)

    @staticmethod
    def clean_numero(numero):
        # Remove espaços em branco extras e converte para maiúsculas
        numero = numero.strip().upper()

        # Verifica se o número do contêiner segue o padrão ISO 6346
        pattern = re.compile(r'^[A-Z]{4}\d{7}$')
        if not pattern.match(numero):
            raise ValidationError(('Número do contêiner deve seguir o padrão ISO 6346: quatro letras seguidas de sete dígitos.'))

        return numero

    def save(self, *args, **kwargs):
        self.full_clean()  # Validação completa antes de salvar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero
