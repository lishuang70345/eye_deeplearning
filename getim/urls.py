from django.conf.urls import url
from . import views

urlpatterns = [
    url('getim', views.getim)
]