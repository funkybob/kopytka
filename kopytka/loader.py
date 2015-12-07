from django.template import Origin, TemplateDoesNotExist
from django.template.loaders.base import Loader

from .models import Template


class DBLoader(Loader):

    def get_contents(self, origin):
        return Template.objects.get(pk=origin.name).content

    def get_template_sources(self, template_name):
        for tmpl in Template.objects.filter(name=template_name):
            yield Origin(name=tmpl.pk, template_name=template_name, loader=self)

    def load_template_source(self, template_name, template_dirs=None):
        try:
            return (Template.objects.get(name=template_name).content, template_name)
        except Template.DoesNotExist:
            raise TemplateDoesNotExist(template_name)

    def load_template(self, template_name, template_dirs=None):
        try:
            return (Template.objects.get(name=template_name), template_name)
        except Template.DoesNotExist:
            raise TemplateDoesNotExist(template_name)
