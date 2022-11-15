
from django.urls import path, include
from . import views

urlpatterns = [
    path("akad/", views.akad_view, name="akad"),
]