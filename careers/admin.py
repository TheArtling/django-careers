"""Admin classes for the careers app."""
from django.contrib import admin

from . import models


class CareerPositionAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'is_published', ]
    list_editable = ['is_published', ]
    exclude = ('slug', )

admin.site.register(models.CareerPosition, CareerPositionAdmin)
