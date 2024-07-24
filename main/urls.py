from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from .views import(
    Home,

    cadastro_motorista,
    lista_motorista,
    motorista_novo,
    motorista_update,

    cadastro_carga,
    lista_carga,
    carga_novo,
    carga_update,

    cadastro_container,
    lista_container,
    container_novo,
    container_update,

    cadastro_desunitizacao,
    lista_desunitizacao,
    desunitizacao_novo,
    desunitizacao_update,

    cadastro_cedido,
    lista_cedido,
    cedido_novo,
    cedido_update,

    relatorio,
)


urlpatterns = [
    path('', Home, name="main_home"),

    path('motoristas', cadastro_motorista, name="main_cadastro_motorista"),
    path('lista-motorista', lista_motorista, name="main_lista_motorista"),
    path('motorista-novo/', motorista_novo, name='main_motorista_novo'),
    re_path(r'motorista-update/(?P<id>\d+)/$', motorista_update, name='main_motorista_update'),

    path('container', cadastro_container, name="main_cadastro_container"),
    path('lista-container', lista_container, name="main_lista_container"),
    path('container-novo', container_novo, name='main_container_novo'),
    re_path(r'container-update/(?P<id>\d+)/$', container_update, name='main_container_update'),

    path('carga', cadastro_carga, name="main_cadastro_carga"),
    path('lista-carga', lista_carga, name="main_lista_carga"),
    path('carga-novo', carga_novo, name='main_carga_novo'),
    re_path(r'carga-update/(?P<id>\d+)/$', carga_update, name='main_carga_update'),

    path('desunitizacao', cadastro_desunitizacao, name="main_cadastro_desunitizacao"),
    path('lista-desunitizacao', lista_desunitizacao, name="main_lista_desunitizacao"),
    path('desunitizacao-novo', desunitizacao_novo, name='main_desunitizacao_novo'),
    re_path(r'desunitizacao-update/(?P<id>\d+)/$', desunitizacao_update, name='main_desunitizacao_update'),

    path('cedido', cadastro_cedido, name="main_cadastro_cedido"),
    path('lista-cedido', lista_cedido, name="main_lista_cedido"),
    path('cedido-novo', cedido_novo, name='main_cedido_novo'),
    re_path(r'cedido-update/(?P<id>\d+)/$', cedido_update, name='main_cedido_update'),

    path('relatorio', relatorio, name="main_relatorio"),
]