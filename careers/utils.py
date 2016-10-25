from django.utils.text import slugify


def create_object_slug(obj, title_field):
    """Creates a slug for a given object, and checks, if it's unique."""
    Model = obj._meta.model
    title = getattr(obj, title_field)
    slug = slugify(title)
    if not slug.replace('-', ''):
        # If someone uses only slug-incompatible letters
        slug = slugify(Model._meta.verbose_name)
    objects = Model.objects.filter(slug=slug)
    if obj.pk:
        objects = objects.exclude(pk=obj.pk)
    number = 0
    while objects.exists():
        number += 1
        slug = u'{}-{}'.format(slugify(title), number)
        objects = Model.objects.filter(slug=slug)
        if obj.pk:
            objects = objects.exclude(pk=obj.pk)
    return slug


class SlugifyModelMixin(object):
    title_field = 'title'

    def __init__(self, *args, **kwargs):
        super(SlugifyModelMixin, self).__init__(*args, **kwargs)
        title = getattr(self, self.title_field)
        setattr(self, '_{0}'.format(self.title_field), title)

    def save(self, *args, **kwargs):
        title = getattr(self, self.title_field)
        _title = getattr(self, '_{0}'.format(self.title_field))
        if title != _title or not self.slug:
            self.slug = create_object_slug(self, self.title_field)
        super(SlugifyModelMixin, self).save(*args, **kwargs)
