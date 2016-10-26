"""URLs for the careers app."""
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.CareersView.as_view(), name='careers'),
    url(r'^markdown/', include('django_markdown.urls')),
]
