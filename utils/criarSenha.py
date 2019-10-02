from usuario.models import Instituicao


def criarSenhaAleatoria():
    senha = Instituicao.objects.make_random_password(length=8)
    # passwrod = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
    return senha