from django.contrib import admin

from .models import (
    Transportadora,
    Cliente,
    Carga,
    Container,
    Container_Aurora,
    Conferente,
    Porto,
    TipoContainer,
    Localização,
    Desunitição_e_Unitização,
    Motorista,
    Preenchimento,
    Lacre,
    TipoAvaria,
    AvariaCarga,
    Cedido
)

admin.site.register(Transportadora)
admin.site.register(Cliente)
admin.site.register(Carga)
admin.site.register(Container)
admin.site.register(Porto)
admin.site.register(TipoContainer)
admin.site.register(Localização)
admin.site.register(Desunitição_e_Unitização)
admin.site.register(Conferente)
admin.site.register(Container_Aurora)
admin.site.register(Motorista)
admin.site.register(Preenchimento)
admin.site.register(Lacre)
admin.site.register(TipoAvaria)
admin.site.register(AvariaCarga)
admin.site.register(Cedido)