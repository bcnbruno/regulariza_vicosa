from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q
from .models import Dados, Formulario, TSeptico, Tanque, OpcaoForm, FiltroBAA
from .forms import FirstForm, SecondForm, ThirdForm
import pylab as pl
import math

caminho = ""

def index(request):

    return render(request, 'dados/index.html', {})

def tela2(request):
    
    return render(request, 'dados/tela2.html', {})

def tela3(request):
        
    if request.method == 'POST':
    
        if OpcaoForm.objects.count() != 0:
            OpcaoForm.objects.all().delete() 

        r = request.POST.get("0", "")
        if r == "":  
            op = OpcaoForm(possui_construcao=r)
        else:
            op = OpcaoForm(possui_construcao=r)
        
        op.save()

    return render(request, 'dados/tela3.html', {})

def tela4(request):

    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()
    
    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            logradouro = form['logradouro'].value()
            area = form['area'].value()
            area_planta = form['area_planta'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

    
            f = Formulario(bairro=bairro, logradouro=logradouro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            if str(logradouro) == "ZRU" or str(nome) == "ZRU":
                dado = Dados.objects.get(bairro=bairro) 
            else:
                dado = Dados.objects.get(bairro=bairro, rua=logradouro, nome=nome) 

            opcao = OpcaoForm.objects.get()
            op = opcao.possui_construcao

            if OpcaoForm.objects.count() != 0:
                OpcaoForm.objects.all().delete()

            opcao = OpcaoForm(possui_construcao=op, tela="4")
            opcao.save()

            if str(logradouro) == "ZRU" or str(nome) == "ZRU":

                return render(request, 'dados/tela8_1.html', {'dado':dado})

            if op != "":
                if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                    
                    return render(request, 'dados/tela8.html', {'opcao': opcao})
                
                elif int(num_pav) > dado.num_pav and float(area) < dado.area_min:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". \
                    A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})

                elif int(num_pav) > dado.num_pav:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos." 

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
                
                elif float(area) < dado.area_min:
                    v = "A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
            else:
                return render(request, 'dados/ta_regularizado.html', {})

    else:
        form = FirstForm()

    return render(request, 'dados/tela4.html', {'form': form})

def tela5(request):
    
    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()
    
    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            logradouro = form['logradouro'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            f = Formulario(bairro=bairro, logradouro=logradouro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()
            
            if str(logradouro) == "ZRU" or str(nome) == "ZRU":
                dado = Dados.objects.get(bairro=bairro) 
            else:
                dado = Dados.objects.get(bairro=bairro, rua=logradouro, nome=nome)                 

            opcao = OpcaoForm.objects.get()
            op = opcao.possui_construcao

            if OpcaoForm.objects.count() != 0:
                OpcaoForm.objects.all().delete()

            opcao = OpcaoForm(possui_construcao=op, tela="5")
            opcao.save()

            if str(logradouro) == "ZRU" or str(nome) == "ZRU":

                return render(request, 'dados/tela8_1.html', {})

            if op != "":
                if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                    
                    return render(request, 'dados/tela8.html', {'opcao': opcao})

                elif int(num_pav) > dado.num_pav and float(area) < dado.area_min:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". \
                        A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})

                elif int(num_pav) > dado.num_pav:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
                
                elif float(area) < dado.area_min:
                    v = "A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
            else:
                return render(request, 'dados/ta_regularizado.html', {})

    else:
        form = FirstForm()

    return render(request, 'dados/tela5.html', {'form': form})

def tela6(request):
    return render(request, 'dados/tela6.html', {})

def tela7(request):
    return render(request, 'dados/tela7.html', {})

def tela8(request):
    return render(request, 'dados/tela8.html', {})

def tela8_1(request):
    return render(request, 'dados/tela8_1.html', {})

def tela10(request):

    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()

    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            logradouro = form['logradouro'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            f = Formulario(bairro=bairro, logradouro=logradouro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()
            
            if str(logradouro) == "ZRU" or str(nome) == "ZRU":
                dado = Dados.objects.get(bairro=bairro) 
            else:
                dado = Dados.objects.get(bairro=bairro, rua=logradouro, nome=nome)    

            opcao = OpcaoForm.objects.get()
            op = opcao.possui_construcao

            if str(logradouro) == "ZRU" or str(nome) == "ZRU":

                return render(request, 'dados/tela8_1.html', {})

            if op != "":
                if OpcaoForm.objects.count() != 0:
                    OpcaoForm.objects.all().delete()

                opcao = OpcaoForm(possui_construcao=op, tela="10")
                opcao.save()

                if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
                    
                    return render(request, 'dados/tela8.html', {'opcao': opcao})

                elif int(num_pav) > dado.num_pav and float(area) < dado.area_min:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". \
                        A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})

                elif int(num_pav) > dado.num_pav:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
                
                elif float(area) < dado.area_min:
                    v = "A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
            else:
                return render(request, 'dados/ta_regularizado.html', {})

    else:
        form = FirstForm()

    return render(request, 'dados/tela10.html', {'form': form})

def tela11(request):
    
    if Formulario.objects.count() != 0:
        Formulario.objects.all().delete()

    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            
            bairro = form['bairro'].value()
            nome = form['nome'].value()
            logradouro = form['logradouro'].value()
            area = form['area'].value()
            area_planta = form['area'].value()
            num_pav = form['num_pav'].value()
            num_pessoas = form['num_pessoas'].value()

            f = Formulario(bairro=bairro, logradouro=logradouro, nome=nome, area=area, area_planta=area_planta, num_pav=num_pav, num_pessoas=num_pessoas)
            f.save()

            if str(logradouro) == "ZRU" or str(nome) == "ZRU":
                dado = Dados.objects.get(bairro=bairro) 
            else:
                dado = Dados.objects.get(bairro=bairro, rua=logradouro, nome=nome)    

            opcao = OpcaoForm.objects.get()
            op = opcao.possui_construcao

            if str(logradouro) == "ZRU" or str(nome) == "ZRU":

                return render(request, 'dados/tela8_1.html', {})

            if op != "":
                if OpcaoForm.objects.count() != 0:
                    OpcaoForm.objects.all().delete()

                opcao = OpcaoForm(possui_construcao=op, tela="11")
                opcao.save()

                if int(num_pav) <= dado.num_pav and float(area) >= dado.area_min:
            
                    return render(request, 'dados/tela8.html', {'opcao': opcao})

                elif int(num_pav) > dado.num_pav and float(area) < dado.area_min:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". \
                        A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})    

                elif int(num_pav) > dado.num_pav:
                    v = "A sua construção possui mais pavimentos do que o exigido pela lei 1420/2000 \
                    para a zona que está localizado, o número máximo de pavimentos \
                    para essa zona é " + str(dado.num_pav) + ". Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
                
                elif float(area) < dado.area_min:
                    v = "A construção possui área menor que a exigida pela lei 1420/2000 \
                    para a zona que está localizado, a área mínima para essa zona é \
                    " + str(dado.area_min) + " metros quadrados. Em caso de dúvidas procure o IPLAM para\
                    melhores esclarecimentos."

                    return render(request, 'dados/naoehpossivel.html', {'value': v})
            else:
                return render(request, 'dados/ta_regularizado.html', {})
  
    else:
        form = FirstForm()

    return render(request, 'dados/tela11.html', {'form': form})

def tela12(request):
    return render(request, 'dados/tela12.html', {})

def tela13(request):
    f = Formulario.objects.get()    
    l = f.logradouro

    return render(request, 'dados/tela13.html', {'l':l})

def tela14(request):
    f = Formulario.objects.get()    
    l = f.logradouro

    return render(request, 'dados/tela14.html', {'l':l})

def tela15(request):
    f = Formulario.objects.get()    
    l = f.logradouro

    return render(request, 'dados/tela15.html', {'l':l})

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

def calc_volume(pessoas):
    v = round((1000 + (pessoas * 145)), 2)
    a = round((v / 2800), 2)
    p = 3.1
    d = round(((4*a)/math.pi)**(1/2),2)

    return v, a, p, d

def calc_volume_f(pessoas):
    v = round( (pessoas * 1.6 * 0.5 * 160) / 1000 , 2)
    a = round((v / 1.2), 2)
    d = round(((4*a)/math.pi)**(1/2), 2)

    return v, a, d

def tela17(request):
    f = Formulario.objects.get()
    pessoas = f.num_pessoas    

    texto = ''

    if int(pessoas) <= 100:
        tanque = TSeptico.objects.get(num_pessoas=pessoas)
        volume = tanque.volume_util_M        
        area = float(tanque.area.replace(",", "."))
        profundidade = round((float( str(tanque.alt_adotada).replace(",", ".") ) + 0.30), 1)
        diametro = tanque.diametro.replace(",", ".")
        comp, larg = comprimento(area)

        filtro = FiltroBAA.objects.get(num_pessoas=pessoas)
        vol_f = round(float(filtro.volume_util_M.replace(",", ".")), 2)
        area_f = float(filtro.area.replace(",", "."))
        diametro_f = float(filtro.diametro.replace(",", "."))
    else:
        volume, area, profundidade, diametro = calc_volume(pessoas)
        comp, larg = comprimento(area)
        texto = 'Para locais com mais de 100 pessoas, pode-se utilizar uma configuração de tanques e filtros em paralelo \
        , poupando assim mais espaço. Por exemplo, se existem 150 pessoas pode-se fazer dois tanques de volume para 75 \
        pessoas e dois filtros de volume para 75 pessoas. Mas ressaltamos que é recomendável buscar um profissional da \
        área de saneamento para o correto dimensionamento e a melhor instrução para a construção de um sistema de maior demanda.'
        vol_f, area_f, diametro_f = calc_volume_f(pessoas)
        
    c = zip(comp,larg)
    

    return render(request, 'dados/tela17.html', {'vol_f':vol_f,'area_f':area_f,'diametro_f':diametro_f, 'texto':texto, 'c':c, 'pessoas':pessoas, 'volume':volume, 'profundidade':profundidade, 'diametro':diametro, 'area':area, 'comp':comp, 'larg':larg})



def tela18(request):
    return render(request, 'dados/tela18.html', {})

def naoehpossivel(request):
 
    return render(request, 'dados/naoehpossivel.html', {})
    
def docconstrucao(request):    
    opcao = OpcaoForm.objects.get()
    tela = opcao.tela
    f = Formulario.objects.get()    
    l = f.logradouro

    return render(request, 'dados/docconstrucao.html', {'l':l, 'tela':tela})
    

def docconstrucao_2(request):    
    opcao = OpcaoForm.objects.get()

    return render(request, 'dados/docconstrucao_2.html', {'opcao':opcao})

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
    logradouro = f.logradouro
    dados = Dados.objects.get(bairro=bairro, rua=logradouro, nome=nome) 

    ar_arPlanta = round( ((f.area_planta / f.area)*100), 2) 
    tx_area = (dados.taxa_prm/100) * f.area_planta
    cp_area = (f.area_planta * f.num_pav) / f.area
    caprov = float(str(dados.coef_aprov).replace(",", ".")) 
    #cp_area = f.area_planta

    return render(request, 'dados/orientacao_ocupacao.html', {'cp_area':cp_area, 'tx_area':tx_area, 'dados':dados, 'ar_arPlanta': ar_arPlanta, 'form':f})

def doc_saae(request):
    f = Formulario.objects.get()    
    l = f.logradouro

    return render(request, 'dados/doc_saae.html', {'l':l})

def pocos(request):
    f = Formulario.objects.get()
    n = (int(f.num_pessoas) * 190 )/ 1000

    return render(request, 'dados/pocos.html', {'n':n})

def emissao_habitasse(request):
    
    return render(request, 'dados/emissao_habitasse.html', {})

def emissao_habitasse_2(request):
    
    return render(request, 'dados/emissao_habitasse_2.html', {})

def emissao_alvara_const(request):
    
    return render(request, 'dados/emissao_alvara_const.html', {})

def emissao_alvara_const_2(request):
    
    return render(request, 'dados/emissao_alvara_const_2.html', {})

def emissao_alvara(request):
    
    return render(request, 'dados/emissao_alvara.html', {})

def proj_arq(request):
    
    return render(request, 'dados/proj_arq.html', {})

def volume_captacao(area):
    return area * 852 * 6 * 0.042

def cap_agua_chuva(request):
    volume = '__'
    telhado = ''
    if request.method == 'POST':
        form = SecondForm(request.POST)
        
        if form.is_valid():
            render(request, 'dados/cap_agua_chuva.html', {'form': form, 'v':volume})
            telhado = float(form['telhado'].value())
            volume = round( volume_captacao(telhado), 2 )

    else:
        form = SecondForm()

    return render(request, 'dados/cap_agua_chuva.html', {'form': form, 'v':volume, 'telhado':telhado} )

def get_vazao(num_pessoas, c):
    if c == 1:
        vazao = (float(num_pessoas) * 160)/1000
    elif c == 2:
        vazao = (float(num_pessoas) * 96)/1000

    return vazao

def get_area(v, c):
    if c == 1:
        return ( v * (math.log1p(75) - math.log1p(30)) ) / (1.025 * 0.5 * 0.4) 
    elif c == 2:
        return ( v * (math.log1p(100) - math.log1p(30)) ) / (1.025 * 0.5 * 0.4)

def wetlands(request):
    f = Formulario.objects.get()
    num_pessoas = float(f.num_pessoas)
    vazao = round(get_vazao(num_pessoas, 1), 2)
    area = round(get_area(vazao, 1), 2)
    comp, larg = comprimento(area)
    
    c = zip(comp,larg)

    return render(request, 'dados/wetlands.html', {'c':c, 'area':area, 'comp':comp, 'larg':larg})

def wetlands_2(request):
    f = Formulario.objects.get()
    num_pessoas = float(f.num_pessoas)
    vazao = round(get_vazao(num_pessoas, 2), 2)
    area = round(get_area(vazao, 2), 2)
    comp, larg = comprimento(area)
    
    c = zip(comp,larg)

    return render(request, 'dados/wetlands_2.html', {'c':c, 'area':area, 'comp':comp, 'larg':larg})


def tanque_evapo(request):
    
    if request.method == 'POST':
        form = ThirdForm(request.POST)
        
        if form.is_valid():

            num_pessoas = float(form['num_pessoas'].value())

            cimento = int(float(num_pessoas) * 1)
            tela = round((float(num_pessoas) * 2.6), 1)
            pneu = (float(num_pessoas) * 4)
            areia_media = round((float(num_pessoas) * 0.3), 1)
            areia_fina = round((float(num_pessoas) * 0.1), 1)
            brita = round((float(num_pessoas) * 0.4), 1)
            imper = round((float(num_pessoas) * 0.4), 1)
            grampo = round((float(num_pessoas) * 0.2), 1)
            t_pvc = round((float(num_pessoas) * 0.2), 1)
            cap_pvc = round((float(num_pessoas) * 0.4), 1)
            return render(request, 'dados/tanque_evapo.html', {'form':form,'n':num_pessoas, 'cimento':cimento, 'tela': tela, 'pneu':pneu, 'areia_media':areia_media, 'areia_fina':areia_fina, 'brita':brita, 'imper':imper, 'grampo': grampo, 't_pvc':t_pvc, 'cap_pvc':cap_pvc})


    else:
        form = ThirdForm()
    
    return render(request, 'dados/tanque_evapo.html', {'form':form})

def biodigestores(request):
    
    return render(request, 'dados/biodigestores.html', {})

def docloteamentos(request):
    
    return render(request, 'dados/docloteamentos.html', {})

def ta_regularizado(request):
    
    return render(request, 'dados/ta_regularizado.html', {})

def reg_obras(request):
    
    return render(request, 'dados/reg_obras.html', {})

def d_construir(request):
    
    return render(request, 'dados/d_construir.html', {})

def corte_arvore(request):
    
    return render(request, 'dados/corte_arvore.html', {})

def emissao_terraplanagem(request):
    
    return render(request, 'dados/emissao_terraplanagem.html', {})

def p_solo(request):
    
    return render(request, 'dados/p_solo.html', {})

def p_solo_f(request):
    
    return render(request, 'dados/p_solo_f.html', {})

def emissao_a_lot(request):
    
    return render(request, 'dados/emissao_a_lot.html', {})

def alvara_urb(request):
    
    return render(request, 'dados/alvara_urb.html', {})


