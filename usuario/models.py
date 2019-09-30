from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from utils.opcoesUsuarios import tipoInstituicao


class InstituicaoManager(BaseUserManager):
    def _create_user(self, email=None, senha=None, **extra_fields):
        if not email:
            raise ValueError('Usuário deve ter um email.')
        email = self.normalize_email(email)
        usuario = self.model(email=email, senha=senha, **extra_fields)

        usuario.set_password(senha)
        usuario.save(using=self.db)
        return usuario

    def create_user(self, email=None, senha=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, senha=senha, **extra_fields)

    def create_superuser(self, email, senha, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email=email, senha=senha, **extra_fields)


class Instituicao(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    senha = models.CharField(max_length=255, null=True, blank=True)
    razaoSocial = models.CharField(verbose_name="Razão Social")
    cnpj = models.CharField(verbose_name="CNPJ")
    telefone = models.CharField(verbose_name="Telefone")
    responsavel = models.CharField(verbose_name="Responsavel")
    tipo = models.CharField(verbose_name="Tipo", max_length=20, choices=tipoInstituicao)
    estado = models.CharField(verbose_name="Estado")
    cidade = models.CharField(verbose_name="Cidade")

    is_superuser = models.NullBooleanField(default=False)

    objects = InstituicaoManager()
    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = '__all__'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['email']

    def __str__(self):
        return self.email

