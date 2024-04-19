from django.urls import path
from . import views
from .views import Home
from django.views.generic.base import RedirectView

from django.conf import settings

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('favicon.ico', RedirectView.as_view(url=''), name='favicon'),
]