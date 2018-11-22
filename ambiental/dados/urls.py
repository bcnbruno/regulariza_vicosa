from django.urls import path
from . import views

app_name = 'dados'

urlpatterns = [
    path('', views.index, name='index'),
    path('tela2/', views.tela2, name='tela2'),
    path('tela3/', views.tela3, name='tela3'),
    path('tela4/', views.tela4, name='tela4'),
    path('tela5/', views.tela5, name='tela5'),
    path('tela4_2/', views.tela4_2, name='tela4_2'),
    path('tela5_2/', views.tela5_2, name='tela5_2'),
    
    path('tela6/', views.tela6, name='tela6'),
    path('tela7/', views.tela7, name='tela7'),
    path('tela8/', views.tela8, name='tela8'),   
    path('tela10/', views.tela10, name='tela10'),
    path('tela11/', views.tela11, name='tela11'),
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
    path('reciclaveis/', views.reciclaveis, name='reciclaveis'),
    path('organicos/', views.organicos, name='organicos'),
    path('rejeitos/', views.rejeitos, name='rejeitos'),
    path('sumidouro/', views.sumidouro, name='sumidouro'),
    path('tanque/', views.tanque, name='tanque'),
    path('orientacao_ocupacao/', views.orientacao_ocupacao, name='orientacao_ocupacao'),
]