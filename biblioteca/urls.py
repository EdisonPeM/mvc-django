from django.urls import path

from .controllers import AutoresController

urlpatterns = [
    path("", AutoresController.index, name="index"),
    path("<int:some_id>", AutoresController.detail, name="detail"),
]