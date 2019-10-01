from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from usuario.models import Instituicao
from utils.opcoesUsuarios import tipoInstituicao


class InstituicaoChangeForm(UserChangeForm):
    class Meta:
        model = Instituicao
        fields = '__all__'


class InstituicaoSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Instituicao
        fields = ['cnpj', 'email', 'razaoSocial', 'telefone', 'responsavel', 'tipo', 'estado', 'cidade']

    @transaction.atomic
    def save(self, commit=True):
        instituicao = super().save(commit=False)
        instituicao.save()

        return instituicao
