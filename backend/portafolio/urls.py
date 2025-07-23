from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from proyectos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# Solo sirve archivos media en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
