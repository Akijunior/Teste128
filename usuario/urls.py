from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('email/', email, name="email"),
    path('cadastrar-instituicao/', InstituicaoSignUpView.as_view(), name="cadastrarInstituicao"),
]