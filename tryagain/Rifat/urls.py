
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('nirab.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.ABOUT_ME_URL, document_root=settings.ABOUT_ME_ROOT)+static(settings.MAIN_TAMPLATE_URL, document_root=settings.MAIN_TAMPLATE_ROOT)

