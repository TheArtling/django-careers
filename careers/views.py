"""Views for the careers app."""
from django.views.generic import TemplateView

from . import models


class CareersView(TemplateView):
    template_name = 'careers/careers_view.html'

    def get_context_data(self, **kwargs):
        ctx = super(CareersView, self).get_context_data(**kwargs)
        ctx.update({
            'careers': models.CareerPosition.objects.filter(
                is_published=True).order_by('position')
        })
        return ctx
