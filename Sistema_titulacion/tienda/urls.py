from django.urls import path

from .views import (crear_empresa)

urlpatterns = [
    path('dashboard/crear/', crear_empresa, name="crear_empresa"),
]