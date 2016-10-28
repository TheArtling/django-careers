"""Models for the careers app."""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_markdown.models import MarkdownField
from django.utils.text import slugify


class CareerPosition(models.Model):
    """
    Career Position information

    :title:             Career title.
    :position:          Position in list.
    :job_description:   Full career description.
    :is_published:      Published status of career.
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=1024,
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

    def slug(self):
        """" Returns computed slug """
        return slugify(
            '{} {}'.format(self.pk, self.title), allow_unicode=True)
