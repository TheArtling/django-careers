"""URLs for the careers app."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CareersView.as_view(), name='careers'),
]
