from django.contrib import admin
from django.urls import path, include

from Teste128Bits import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
