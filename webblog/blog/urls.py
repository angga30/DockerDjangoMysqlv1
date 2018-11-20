from django.urls import path
from . import views as blogvw

urlpatterns = [
    path('',blogvw.index),
]