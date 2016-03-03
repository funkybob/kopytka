from django.db import models

from .transforms import SKeys


class PageQuerySet(models.QuerySet):

    def published(self):
        return self.filter(is_published=True)

    def fragment_keys(self):
        return self.annotate(keys=SKeys('fragments')).values_list('keys', flat=True).distinct()
