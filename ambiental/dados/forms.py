from django import forms
 
# Importa modelo
from .models import Dados, Formulario
 
def get_field(st):
    choices = ()
    for choice in Dados.objects.values(st).distinct().order_by(st):
        choices = choices + ((choice[st], choice[st]),)
    
    return choices

# Cria classe do form para o modelo
class FirstForm(forms.Form):
    bairro = forms.ChoiceField(widget=forms.Select(attrs={"style": "width: 500px"}), choices=get_field('bairro'))
    nome = forms.ChoiceField(widget=forms.Select(attrs={"style": "width: 500px"}), choices=get_field('nome'))
    area = forms.FloatField(widget=forms.TextInput(attrs={'size': '20'}))
    area_planta = forms.FloatField(widget=forms.TextInput(attrs={'size': '20'}))
    num_pav = forms.IntegerField(widget=forms.TextInput(attrs={'size': '20'}))
    num_pessoas = forms.IntegerField(widget=forms.TextInput(attrs={'size': '20'}))

class CondVertForm(forms.Form):
    num_lotes = forms.IntegerField(widget=forms.TextInput(attrs={'size': '20'}))
    num_predios = forms.IntegerField(widget=forms.TextInput(attrs={'size': '20'}))

class SecondForm(forms.Form):
    telhado = forms.FloatField()  

class ThirdForm(forms.Form):
    num_pessoas = forms.IntegerField()     