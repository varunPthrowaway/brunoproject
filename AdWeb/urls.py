from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adtool.urls')),
    path('', include('users.urls')),
    path('password-reset/done', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
        ), 
        name='password_reset_confirm'
    ),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

]

"""
FOR PRODUCTION REMOVE ELSE AND CHANGE SETTINGS TO USE A FILE-SERVER
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
