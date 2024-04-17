from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', include('admin_acessos.urls')),
    path('admin/', admin.site.urls),    
    path('rh/', include('rh.urls')),
    path('', include('gestao_escolar.urls')),
    path('nutricao/', include('controle_estoque.urls')),
    path('central_admin/', include('admin_acessos.urls')),


]
