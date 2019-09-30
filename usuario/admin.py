from django.apps import apps
from django.contrib import admin

register_all_models_from = [
    'usuario',
    'propriedade'
]

for app in register_all_models_from:
    for name, obj in apps.all_models[app].items():
        admin.site.register(obj)