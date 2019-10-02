from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from django.views.generic import CreateView

from usuario.forms import InstituicaoSignUpForm
from usuario.models import Instituicao

@login_required
def index(request):
    return render(request, 'index.html')

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['suitsu19@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('index')

class InstituicaoSignUpView(CreateView):
    model = Instituicao
    form_class = InstituicaoSignUpForm
    template_name = 'registration/cadastrarInstituicao.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')