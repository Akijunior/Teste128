from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from utils.opcoesUsuarios import tipoInstituicao


class InstituicaoManager(BaseUserManager):
    def _create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Usuário deve ter um email.')
        email = self.normalize_email(email)
        usuario = self.model(email=email, password=password, **extra_fields)

        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email=email, password=password, **extra_fields)


class Instituicao(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    razaoSocial = models.CharField(verbose_name="Razão Social", max_length=255,)
    cnpj = models.CharField(verbose_name="CNPJ", max_length=255, unique=True)
    telefone = models.CharField(verbose_name="Telefone", max_length=255,)
    responsavel = models.CharField(verbose_name="Responsavel", max_length=255,)
    tipo = models.CharField(verbose_name="Tipo", max_length=20, choices=tipoInstituicao)
    estado = models.CharField(verbose_name="Estado", max_length=255)
    cidade = models.CharField(verbose_name="Cidade", max_length=255)

    is_superuser = models.NullBooleanField(default=False)
    is_staff = models.NullBooleanField(default=True, blank=True, null=True)

    objects = InstituicaoManager()
    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'
        ordering = ['email']

    def __str__(self):
        return self.email