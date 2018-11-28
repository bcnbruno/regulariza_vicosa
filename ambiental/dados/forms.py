from django import forms
 
# Importa modelo
from .models import Dados, Formulario
 
def get_field(st):
    choices = ()
    if st != 'bairro':
        choices = (('ZRU', 'ZRU'),)
    for choice in Dados.objects.values(st).distinct().order_by(st):
        choices = choices + ((choice[st], choice[st]),)
    
    return choices

def get_logradouro():
    choices = (
        ('Rua', 'Rua'),
        ('Travessa', 'Travessa'),
        ('Avenida', 'Avenida'),
        ('Praça', 'Praça'),
        ('Estrada', 'Estrada'),
        ('Outros', 'Outros'),
        ('Beco', 'Beco'),
        ('Vila', 'Vila'),
        ('Sítio', 'Sítio'),
        ('Rodovia', 'Rodovia'), 
        ('Fazenda', 'Fazenda'),
        ('Condomínio', 'Condomínio'),
        ('Alameda', 'Alameda'),
        ('ZRU', 'ZRU'),
    )
    return choices

# Cria classe do form para o modelo
class FirstForm(forms.Form):
    bairro = forms.ChoiceField(widget=forms.Select(attrs={"style": "width: 300px"}), choices=get_field('bairro'))
    nome = forms.ChoiceField(widget=forms.Select(attrs={"style": "width: 300px"}), choices=get_field('nome'))
    logradouro = forms.ChoiceField(widget=forms.Select(attrs={"style": "width: 300px"}), choices=get_logradouro())
    area = forms.FloatField(widget=forms.TextInput(attrs={'size': '20'}))
    area_planta = forms.FloatField(widget=forms.TextInput(attrs={'size': '20'}))
    num_pav = forms.IntegerField(widget=forms.TextInput(attrs={'size': '20'}))
    num_pessoas = forms.IntegerField(widget=forms.TextInput(attrs={'size': '20'}))

class SecondForm(forms.Form):
    telhado = forms.FloatField()  

class ThirdForm(forms.Form):
    num_pessoas = forms.IntegerField()     