from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from usuario.forms import InstituicaoSignUpForm
from usuario.models import Instituicao

@login_required
def index(request):
    return render(request, 'index.html')

class InstituicaoSignUpView(CreateView):
    model = Instituicao
    form_class = InstituicaoSignUpForm
    template_name = 'registration/cadastrarInstituicao.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')