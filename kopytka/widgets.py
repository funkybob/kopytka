from django import forms
from django.contrib.admin.templatetags.admin_static import static


class HStoreWidget(forms.Textarea):

    @property
    def media(self):
        return forms.Media(js=[static('kopytka/js/hstore.js')])

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = 'hstore'
        return super(HStoreWidget, self).render(name, value, attrs)
