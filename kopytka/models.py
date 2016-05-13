from django.conf import settings
from django.contrib.postgres.fields import HStoreField
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Template as DjangoTemplate
from django.utils.functional import cached_property
from scss.compiler import Compiler
from scss.errors import SassSyntaxError

from . import managers


class Page(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    path = models.SlugField(blank=True)
    order = models.PositiveIntegerField(default=0)

    title = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)

    template = models.ForeignKey('Template', blank=True, null=True)

    content = models.TextField(blank=True)
    fragments = HStoreField(blank=True)

    objects = managers.PageQuerySet.as_manager()

    def __str__(self):
        return '{} : {}'.format(self.url, self.title)

    class Meta:
        unique_together = (
            ('parent', 'path'),
        )

    def get_absolute_url(self):
        paths = [self.path]
        node = self.parent
        while node:
            paths.insert(0, node.path)
            node = node.parent
        return '/%s' % '/'.join(paths)
    get_absolute_url.short_description = 'url'

    @cached_property
    def url(self):
        return self.get_absolute_url()

    def get_template(self):
        obj = self
        while obj:
            if obj.template_id:
                return obj.template
            if not obj.parent_id:
                return 'default.html'
            obj = obj.parent

    def __getitem__(self, key):
        return self.fragments[key]


class Template(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def render(self, context):
        return DjangoTemplate(self.content).render(context)


class StyleSheet(models.Model):
    name = models.SlugField()
    description = models.CharField(max_length=500, blank=True)
    source = models.TextField(blank=True)
    output = models.TextField(blank=True, editable=False)
    minify = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '.css'

    def get_absolute_url(self):
        return reverse('kopytka:style-sheet', kwargs={'name': self.name})

    def clean(self):
        compiler = Compiler(search_path=getattr(settings, 'SASS_SEARCH_PATHS', []),
                            output_style='compressed' if self.minify else 'nested')
        try:
            self.output = compiler.compile_string(self.source)
        except (ValueError, SassSyntaxError) as e:
            import traceback ; traceback.print_exc()
            raise ValidationError({'source': str(e)})
