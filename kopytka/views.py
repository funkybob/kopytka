from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from . import models


def page(request, path):

    paths = list(filter(None, path.split('/'))) or ['', ]

    paths.reverse()

    query = {}
    pfx = 'path'
    for step in paths:
        query[pfx] = step
        pfx = 'parent__%s' % pfx
    query[pfx.replace('path', 'isnull')] = True

    try:
        page = models.Page.objects.published().get(**query)
    except models.Page.DoesNotExist:
        raise Http404

    return render(request, page.get_template(), {'page': page})


def style_sheet(request, name):
    sheet = get_object_or_404(models.StyleSheet, name=name)

    return HttpResponse(sheet.output, content_type='text/css')
