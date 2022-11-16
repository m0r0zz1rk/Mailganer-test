from django.contrib import admin
from django.urls import path, include

from mail.api import PixelViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/subs/', include('users.urls')),
    path('api/temps/', include('templates.urls')),
    path('api/mailing/', include('mail.urls')),
    path('tracking/<int:id>/<str:email>/', PixelViewSet.as_view({'get': 'AddOpenMail'}))
]
