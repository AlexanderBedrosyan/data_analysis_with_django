from django.urls import path
from . import views
from .views import Home

from django.conf import settings

urlpatterns = [
    path('', Home.as_view(), name='home'),
]