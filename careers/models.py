"""Models for the careers app."""

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django_markdown.models import MarkdownField

from utils import SlugifyModelMixin


class CareerPosition(SlugifyModelMixin, models.Model):
    """
    Career Position information

    :title:             Career title.
    :slug:              The slugified title.
    :position:          Position in list.
    :job_description:   Full career description.
    :is_published:      Published status of career.
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=1024,
    )
    slug = models.CharField(
        verbose_name=_('Slug'),
        max_length=1024,
        blank=True,
    )
    position = models.IntegerField(
        verbose_name=_('Position'),
    )
    job_description = MarkdownField(
        verbose_name=_('Job Description'),
        blank=True,
    )
    is_published = models.BooleanField(
        verbose_name=_('Is published'),
        default=False,
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(CareerPosition, self).save(*args, **kwargs)
