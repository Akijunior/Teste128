from django.contrib.auth.models import User
from rest_framework import serializers

from propriedade.models import Propriedade
from usuario.models import Instituicao


class PropriedadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Propriedade
        fields = '__all__'


class InstituicaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instituicao
        fields = ['cnpj', 'email', 'razaoSocial', 'telefone', 'responsavel', 'tipo', 'estado', 'cidade']