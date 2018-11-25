from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q
from .models import Dados, Formulario, TSeptico, Tanque
from .forms import FirstForm
import pylab as pl

opcaoEscolhida = ""
caminho = ""

def index(request):
    #dados = Dados.objects.values() 
    return render(request, 'dados/index.html', {})

def tela2(request):
    
    return render(request, 'dados/tela2.html', {})

def tela3(request):
    r = request.POST.get("0", " ")
    global opcaoEscolhida 
    opcaoEscolhida = r
    return render(request, 'dados/tela3.html', {'op':opcaoEscolhida})

def tela4(request):

    global opcaoEscolhida 

    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area_planta'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="4"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 
            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela4.html', {'form': form, 'op':opcaoEscolhida})

def tela4_2(request):

    global opcaoEscolhida 

    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="4"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 
            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela4.html', {'form': form, 'op':opcaoEscolhida})


def tela5(request):
    
    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="5"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 

            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela5.html', {'form': form})

def tela5_2(request):
    
    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="5"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 

            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela5.html', {'form': form})


def tela6(request):
    return render(request, 'dados/tela6.html', {})

def tela7(request):
    return render(request, 'dados/tela7.html', {})

def tela8(request):
    return render(request, 'dados/tela8.html', {})

def tela10(request):

    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="10"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 

            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela10.html', {'form': form})

def tela10_2(request):

    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="10"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 

            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela10.html', {'form': form})

def tela11(request):
    
    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="11"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 

            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela11.html', {'form': form})

def tela11_2(request):
    
    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirstForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            global caminho
            caminho="11"

            f = Formulario(bairro=bairro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            dado = Dados.objects.get(bairro=bairro, nome=nome) 

            if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                return HttpResponseRedirect('../tela8/')
            elif int(num_pav) > dado.num_pav:
                return render(request, 'dados/naoehpossivel.html', {'value': dado.num_pav})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FirstForm()

    return render(request, 'dados/tela11.html', {'form': form})


def tela12(request):
    return render(request, 'dados/tela12.html', {})

def tela13(request):
    return render(request, 'dados/tela13.html', {})

def tela14(request):
    return render(request, 'dados/tela14.html', {})

def tela15(request):
    return render(request, 'dados/tela15.html', {})

def tela16(request):
    return render(request, 'dados/tela16.html', {})

def comprimento(area):
    comp = []
    larg = []
    for l in pl.frange(0.8, 100, 0.2):
        c = round((area / l),1)
        if (c / l) >= 2 and (c / l) <= 4:
            comp.append(round(c, 2))
            larg.append(round(l, 2))
    return comp, larg

def tela17(request):
    f = Formulario.objects.get()

    pessoas = f.num_pessoas

    tanque = TSeptico.objects.get(num_pessoas=pessoas)

    volume = tanque.volume_util_M
    diametro = tanque.diametro.replace(",", ".")
    area = float(tanque.area.replace(",", "."))
    profundidade = float( str(tanque.alt_adotada).replace(",", ".") ) + 0.30
    comp, larg = comprimento(area)
  
    c = zip(comp,larg)
    

    return render(request, 'dados/tela17.html', {'c':c, 'pessoas':pessoas, 'volume':volume, 'profundidade':profundidade, 'diametro':diametro, 'area':area, 'comp':comp, 'larg':larg})



def tela18(request):
    return render(request, 'dados/tela18.html', {})

def naoehpossivel(request):
 
    return render(request, 'dados/naoehpossivel.html', {})
    
def docconstrucao(request):
    global opcaoEscolhida
    global caminho

    return render(request, 'dados/docconstrucao.html', {'op':opcaoEscolhida, 'c':caminho})

def reciclaveis(request):
 
    return render(request, 'dados/reciclaveis.html', {})

def organicos(request):
 
    return render(request, 'dados/organicos.html', {})

def rejeitos(request):
 
    return render(request, 'dados/rejeitos.html', {})

def regularizadosim(request):
 
    return render(request, 'dados/regularizadosim.html', {})

def sumidouro(request):
 
    return render(request, 'dados/sumidouro.html', {})

def orientacao_ocupacao(request):
 
    f = Formulario.objects.get()
    bairro = f.bairro
    nome = f.nome
    dados = Dados.objects.get(bairro=bairro, nome=nome) 

    ar_arPlanta = round( ((f.area_planta / f.area)*100), 2) 
    tx_area = dados.taxa_prm * f.area_planta
    cp_area = float(dados.coef_aprov.replace(",", ".")) * f.area_planta
    #cp_area = f.area_planta

    return render(request, 'dados/orientacao_ocupacao.html', {'cp_area':cp_area, 'tx_area':tx_area, 'dados':dados, 'ar_arPlanta': ar_arPlanta, 'form':f})

def doc_saae(request):

    return render(request, 'dados/doc_saae.html', {})

def pocos(request):
    f = Formulario.objects.get()
    n = (int(f.num_pessoas) * 190 )/ 1000

    return render(request, 'dados/pocos.html', {'n':n})

def emissao_habitasse(request):
    
    return render(request, 'dados/emissao_habitasse.html', {})

def emissao_alvara_const(request):
    
    return render(request, 'dados/emissao_alvara_const.html', {})

def emissao_alvara(request):
    
    return render(request, 'dados/emissao_alvara.html', {})

def proj_arq(request):
    
    return render(request, 'dados/proj_arq.html', {})