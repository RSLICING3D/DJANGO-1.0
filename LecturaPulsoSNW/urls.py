from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from LecturaPulso import views

from urllib.parse import urlparse
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LecturaPulso.urls')),
    path('dashboard/', views.dashboard),
    path('dashboard/Encender/', views.Encender),
    path('dashboard/Apagar/', views.Apagar),
    path('dashboard/Encender1/', views.Encender1),
    path('dashboard/Apagar1/', views.Apagar1),
    path('dashboard/Encender2/', views.Encender2),
    path('dashboard/Apagar2/', views.Apagar2),
    path('dashboard/Encender3/', views.Encender3),
    path('dashboard/Apagar3/', views.Apagar3),
    path('dashboard/Encender4/', views.Encender4),
    path('dashboard/Apagar4/', views.Apagar4),
    path('dashboard/Encender5/', views.Encender5),
    path('dashboard/Apagar5/', views.Apagar5),
    path('dashboard/Encender6/', views.Encender6),
    path('dashboard/Apagar6/', views.Apagar6),
    path('dashboard/Encender7/', views.Encender7),
    path('dashboard/Apagar7/', views.Apagar7),
    path('dashboard/Encender00/', views.Encender00),
    path('dashboard/Apagar00/', views.Apagar00),
    path('dashboard/Encender01/', views.Encender01),
    path('dashboard/Apagar01/', views.Apagar01),
    path('password_reset/', PasswordResetView.as_view(template_name='BusUser.html'), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='passwords_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='passwords_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='passwords_reset_complete.html'), name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


