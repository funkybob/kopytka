from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from . import models


class PageView(generic.DetailView):
    model = models.Page

    def get_queryset(self):
        return models.Page.objects.published().select_related('template')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        paths = list(filter(None, self.kwargs.get('path', '/').split('/'))) or ['', ]

        paths.reverse()

        query = {}
        pfx = 'path'
        for step in paths:
            query[pfx] = step
            pfx = 'parent__%s' % pfx
        query[pfx.replace('path', 'isnull')] = True

        try:
            page = queryset.get(**query)
        except models.Page.DoesNotExist:
            raise Http404
        return page

    def get_template_names(self):
        return self.object.get_template(),


def style_sheet(request, name):
    sheet = get_object_or_404(models.StyleSheet, name=name)

    return HttpResponse(sheet.output, content_type='text/css')
