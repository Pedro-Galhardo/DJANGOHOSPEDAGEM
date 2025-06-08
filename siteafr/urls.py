from django.urls import path
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('doacao/', views.doacao, name='doacao'),
    path('atendimento/', views.atendimento, name='atendimento'),

    path('nossahistoria/', views.nossahistoria, name='nossahistoria'),

    path('governanca/', views.governanca, name='governanca'),

    path('transparencia/', views.transparencia, name='transparencia'),

    path('certificacoes/', views.certificacoes, name='certificacoes'),

    path('reabilitação/', views.reabilitacao, name='reabilitação'),

    path('cooperacao/', views.cooperacao, name='cooperacao'),

    path('sac/', views.sac, name='sac'),

    path('visita/', views.visita, name='visita'),

    path('trabalheconosco/', views.trabalheconosco, name='trabalheconosco'),

    path('voluntariado/', views.voluntariado, name='voluntariado'),

    path('unidadefluminense/', views.unidadefluminense, name='unidadefluminense'),

    path('unidadelisaura/', views.unidadelisaura, name='unidadelisaura'),

    path('afrmais/', views.afrmais, name='afrmais'),

    path('depmedico/', views.depmedico, name='depmedico'),

    path('oficinaorto/', views.oficinaorto, name='oficinaorto'),

    path("sistema-restrito-login/", views.sistema_restrito_login, name="sistema-restrito-login"),
    path("sistema-restrito-crud/", views.sistema_restrito_crud, name="sistema-restrito-crud"),
    path("sistema-restrito-crud/delete/<int:pk>/", views.delete_paciente, name="delete-paciente"),
    path("sistema-restrito-crud/update/<int:pk>/", views.update_paciente, name="update-paciente"),

    path("sistema-restrito-crud/relatorio/", views.gerar_relatorio_historico, name="gerar-relatorio-historico"),

    path('grafico/', views.gerar_grafico, name='gerar-grafico'),

    path('fag/', views.fag, name='fag'),

    path('editais/', views.editais, name='editais'),

    path('parceiroscaptacao/', views.captacao, name='parceiroscaptacao'),

    path('imprensa/', views.imprensa, name='imprensa'),

    path('guia/', views.guia, name='guia'),

    path('privacidade/', views.privacidade, name='privacidade'),






]