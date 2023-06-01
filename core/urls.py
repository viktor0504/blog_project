from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('profile/', include('profiles.urls', namespace='profile')),
    
    #base urls
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)