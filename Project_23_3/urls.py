# Project_23_3/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App_23_3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.resume_view, name='home'),  # Root URL points to resume view
    path('resume/', views.resume_view, name='resume'),  # Keep /resume/ path
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
