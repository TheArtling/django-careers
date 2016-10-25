"""URLs to run the tests."""
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^careers/', include('careers.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
]
