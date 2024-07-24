from django.forms import CheckboxSelectMultiple, DateInput, DateTimeInput, ModelForm
from .models import(Motorista, 
                    Transportadora, 
                    Container, 
                    Carga, 
                    Desunitição_e_Unitização, 
                    Motorista, 
                    Preenchimento, 
                    Cedido)
from django.utils.translation import gettext_lazy as _


class MotoristaForm(ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'


class TransportadoraForm(ModelForm):
    class Meta:
        model = Transportadora
        fields = '__all__'


class ContainerForm(ModelForm):
    class Meta:
        model = Container
        fields = '__all__'
        widgets = {
            'data_entrada': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'data_saida': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'demurrage': DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'avaria': CheckboxSelectMultiple(),
        }



class CargaForm(ModelForm):
    class Meta:
        model = Carga
        fields = '__all__'
        widgets = {
            'data_Lançamento_NF': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'data_entrada': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'data_saida': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'avaria': CheckboxSelectMultiple(),
            
        }


class Desunitição_e_UnitizaçãoForm(ModelForm):
    class Meta: 
        model = Desunitição_e_Unitização
        fields = '__all__'
        widgets = {
            'data_Deslacre': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'data_inicio': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'data_fim': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
        }


class CedidoForm(ModelForm):
    class Meta:
        model = Cedido
        fields = '__all__'
        widgets = {
            'data_saida': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'data_retorno': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
            'avaria': CheckboxSelectMultiple(),
        }