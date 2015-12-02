from django.db import models


class PageQuerySet(models.QuerySet):

    def published(self):
        return self.filter(is_published=True)
