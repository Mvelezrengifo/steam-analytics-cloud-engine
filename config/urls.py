from django.contrib import admin
from django.urls import path
from .views import steam_dashboard # Importamos tu nueva vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', steam_dashboard, name='home'), # La página principal ahora es el Dashboard
]