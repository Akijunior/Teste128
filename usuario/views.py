import json

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from propriedade.models import Propriedade
from usuario.forms import InstituicaoSignUpForm, SolicitarNovaSenhaForm
from usuario.models import Instituicao
from utils.criarSenha import criarSenhaAleatoria


@login_required
def index(request):
    response = requests.get('http://teste.aquabit.com.br/api/v1/propriedades/')

    dicio_json = response.json()
    dicio_string = json.dumps(dicio_json)
    dicio_python = json.loads(dicio_string)

    dicio_user = dicio_python["results"]
    lista = []

    for i in dicio_user:
        for key in i.keys():
            if key in ['id', 'nome', 'estado', 'cnpj',
                           'inscricao_estadual', 'cidade', 'email',
                           'telefone']:
                lista.append(key)
        break
        # print(i["cidade"])

    return render(request, 'index.html', {
        'usuarios': dicio_user,
        'lista': lista,
        'usuario': request.user
    })


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['luijunior96@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False, )
    return redirect('index')


def solicitarNovaSenha(request):
    form = SolicitarNovaSenhaForm(request.POST or None)
    # print(request.POST.get('email'))

    if form.is_valid():

        if Instituicao.objects.filter(email=form.cleaned_data['email']).exists():
            usuario = get_object_or_404(Instituicao, email=form.cleaned_data['email'])
            novaSenha = criarSenhaAleatoria()
            subject = 'Solicitação de Nova Senha'
            message = ' Olá. Você solicitou uma troca de senha e para tanto foi gerado abaixo sua nova senha de ' \
                      'acesso ao sistema.\nNova senha: %s\nObrigado pela atenção. Acesse o link ' \
                      'http://127.0.0.1:8000/ para se conectar conosco. \n' \
                      'Volte sempre. ' % novaSenha
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email'], ]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            usuario.set_password(novaSenha)
            usuario.save()

            messages.success(request, 'Um e-mail com a nova senha foi enviado a sua conta')
            return redirect('login')

        else:
            messages.error(request, 'Não existe nenhum usuário cadastrado com esse e-mail')

    return render(request, 'registration/newPasswordResetForm.html', {'form': form})


class InstituicaoSignUpView(CreateView):
    model = Instituicao
    form_class = InstituicaoSignUpForm
    template_name = 'registration/cadastrarInstituicao.html'

    def form_valid(self, form):
        user = form.save()

        login(self.request, user)
        return redirect('index')