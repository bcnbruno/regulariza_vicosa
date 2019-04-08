from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'dados'

urlpatterns = [
    path('', views.index, name='index'),
    path('tela2/', views.tela2, name='tela2'),
    path('tela3/', views.tela3, name='tela3'),
    path('tela4/', views.tela4, name='tela4'),
    
    path('tela6/', views.tela6, name='tela6'),    
    path('tela8/', views.tela8, name='tela8'), 
    path('tela8_1/', views.tela8_1, name='tela8_1'),    
   
    path('tela12/', views.tela12, name='tela12'),
    path('tela13/', views.tela13, name='tela13'),
    path('tela14/', views.tela14, name='tela14'),
    path('tela15/', views.tela15, name='tela15'),
    path('tela16/', views.tela16, name='tela16'),
    path('tela17/', views.tela17, name='tela17'),
    path('tela18/', views.tela18, name='tela18'),
    
    path('regularizadosim/', views.regularizadosim, name='regularizadosim'),
    path('naoehpossivel/', views.naoehpossivel, name='naoehpossivel'),
    path('docconstrucao/', views.docconstrucao, name='docconstrucao'),
    path('docconstrucao_2/', views.docconstrucao_2, name='docconstrucao_2'),
    path('reciclaveis/', views.reciclaveis, name='reciclaveis'),
    path('organicos/', views.organicos, name='organicos'),
    path('rejeitos/', views.rejeitos, name='rejeitos'),
    path('sumidouro/', views.sumidouro, name='sumidouro'),
    path('orientacao_ocupacao/', views.orientacao_ocupacao, name='orientacao_ocupacao'),
    path('doc_saae/', views.doc_saae, name='doc_saae'),
    path('doc_saae_2', views.doc_saae_2, name='doc_saae_2'),
    path('pocos/', views.pocos, name='pocos'),
    path('emissao_habitasse/', views.emissao_habitasse, name='emissao_habitasse'),
    path('emissao_habitasse_2/', views.emissao_habitasse_2, name='emissao_habitasse_2'),
    path('emissao_alvara_const/', views.emissao_alvara_const, name='emissao_alvara_const'),
    path('emissao_alvara_const_2/', views.emissao_alvara_const_2, name='emissao_alvara_const_2'),
    path('emissao_alvara/', views.emissao_alvara, name='emissao_alvara'),
    path('proj_arq/', views.proj_arq, name='proj_arq'),
    path('cap_agua_chuva/', views.cap_agua_chuva, name='cap_agua_chuva'),
    path('tanque_evapo/', views.tanque_evapo, name='tanque_evapo'),
    path('wetlands/', views.wetlands, name='wetlands'),
    path('wetlands_2/', views.wetlands_2, name='wetlands_2'),
    path('biodigestores/', views.biodigestores, name='biodigestores'),
    path('docloteamentos/', views.docloteamentos, name='docloteamentos'),
    path('ta_regularizado/', views.ta_regularizado, name='ta_regularizado'),
    path('reg_obras/', views.reg_obras, name='reg_obras'),
    path('d_construir/', views.d_construir, name='d_construir'),
    path('corte_arvore/', views.corte_arvore, name='corte_arvore'),
    path('emissao_terraplanagem/', views.emissao_terraplanagem, name='emissao_terraplanagem'),
    path('p_solo/', views.p_solo, name='p_solo'),
    path('p_solo_f/', views.p_solo_f, name='p_solo_f'),
    path('emissao_a_lot/', views.emissao_a_lot, name='emissao_a_lot'),
    path('alvara_urb/', views.alvara_urb, name='alvara_urb'),
    url(r'ajax/escolha_bairro/$', views.escolha_bairro, name='escolha_bairro'),
]