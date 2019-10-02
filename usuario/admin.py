from django.contrib import admin

from usuario.models import Instituicao

admin.site.site_header = "Gerenciador Institucional"
admin.site.site_title = "Gerenciador Institucional"

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ['cnpj', 'razaoSocial', 'email', 'telefone', 'responsavel', 'tipo', 'cidade', 'estado']
    list_filter = ['cidade', 'estado']
    search_fields = ['cnpj', 'responsavel', 'email']
    prepopulated_fields = {'cnpj': ('cnpj',)}
    ordering = ['id', 'cnpj', 'razaoSocial', 'email', 'telefone', 'responsavel', 'tipo', 'cidade', 'estado']
    # fields = [('estado', 'cidade'),]
    fieldsets = (
        ('Localização', {
            'fields': ('estado', 'cidade')
        }),
        ('Contato', {
            'fields': ('responsavel', 'telefone', 'email')
        }),
        ('Detalhes', {
            'fields': ('cnpj', 'tipo', 'razaoSocial')
        }),
    )

admin.site.register(Instituicao , InstituicaoAdmin)