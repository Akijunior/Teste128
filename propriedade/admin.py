from django.apps import apps
from django.contrib import admin


class PropriedadeAdmin(admin.ModelAdmin):
    list_display = ['idApi', 'nome', 'nomeProprietario', 'qtdAtual', 'id']
    list_filter = ('nomeProprietario', 'qtdAtual')

register_all_models_from = [
    'propriedade'
]

for app in register_all_models_from:
    for name, obj in apps.all_models[app].items():
        if (name == 'propriedade'):
            admin.site.register(obj, PropriedadeAdmin)
        # admin.site.register(obj)