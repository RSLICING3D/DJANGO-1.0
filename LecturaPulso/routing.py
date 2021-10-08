from django.urls import path
from .consumers import WSConsumerdashboard

ws_urlpatterns = [
    path('dashboard', WSConsumerdashboard.as_asgi()),

]
