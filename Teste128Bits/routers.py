from rest_framework import routers
from usuario.viewsets import InstituicaoViewSet, PropriedadeViewSet

router = routers.DefaultRouter()
router.register(r'instituicoes', InstituicaoViewSet, base_name='instituicao')
router.register(r'propriedades', PropriedadeViewSet, base_name='propriedade')
