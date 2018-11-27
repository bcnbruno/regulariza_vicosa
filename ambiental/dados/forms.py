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
    bairro = forms.ChoiceField(choices=get_field('bairro'))
    nome = forms.ChoiceField(choices=get_field('nome'))
    area = forms.FloatField()
    area_planta = forms.FloatField()
    num_pav = forms.IntegerField()
    num_pessoas = forms.IntegerField()

class SecondForm(forms.Form):
    telhado = forms.FloatField()  

class ThirdForm(forms.Form):
    num_pessoas = forms.IntegerField()     