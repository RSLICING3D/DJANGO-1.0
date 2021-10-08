from django.urls import path
from .views import dashboard, index, contact, registerPage, loginPage, logoutUser, Message, Int00, Int01, Int02, Int03, Int04

urlpatterns = [
    path('', index),
    path('', dashboard, name='dashboard'),
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('dashboard/Message/', Message, name="Message"),
    path('dashboard/MessageInt0/', Int00, name="MessageInt0"),
    path('dashboard/MessageInt1/', Int01, name="MessageInt1"),
    path('dashboard/MessageInt2/', Int02, name="MessageInt2"),
    path('dashboard/MessageInt3/', Int03, name="MessageInt3"),
    path('dashboard/MessageInt4/', Int04, name="MessageInt4"),
    path('Contacto/', contact, name="Contacto"),
]
