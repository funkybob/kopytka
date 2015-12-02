from django.template import TemplateDoesNotExist
from django.template.loaders.base import Loader

from .models import Template


class DBLoader(Loader):

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
