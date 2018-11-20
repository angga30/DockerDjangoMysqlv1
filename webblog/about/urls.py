from django.urls import path
from .  import views as aboutvw

urlpatterns = [
    path('',aboutvw.index)
]