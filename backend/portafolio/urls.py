from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from proyectos.views import home, detalle_proyecto, sobre_mi 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Página principal
    path('proyecto/<int:id>/', detalle_proyecto, name='detalle_proyecto'),
    path('sobre-mi/', sobre_mi, name='sobre_mi'),
]

# ✅ Sirve archivos multimedia (solo en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
