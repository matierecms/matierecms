from django.conf import settings
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        abstract = True


class TranslatedModel(models.Model):
    language = models.CharField(max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    translation_key = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(fields=['language', 'translation_key'], name='unique_translation_key')
        ]


class TranslatedPageModel(TranslatedModel, Page):

    class Meta:
        abstract = True
