from django.contrib import admin
from django.urls import path

from core inport views

urlpatterns = [
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]

