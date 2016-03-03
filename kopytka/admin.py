from django.contrib import admin

from . import models, widgets


class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'parent', 'order', 'template', 'is_published')
    list_filter = ('is_published',)
    ordering = ('parent', 'order',)

    formfield_overrides = {
        models.HStoreField: {'widget': widgets.HStoreWidget},
    }

    class Media:
        css = {
            'all': (
                'codemirror/lib/codemirror.css',
                'kopytka/css/editor.css',
            ),
        }
        js = (
            'codemirror/lib/codemirror.js',
            'codemirror/addon/mode/overlay.js',
            'codemirror/mode/xml/xml.js',
            'codemirror/mode/htmlmixed/htmlmixed.js',
            'codemirror/mode/django/django.js',
            'kopytka/js/editor.js',
            'kopytka/js/editor_page.js',
        )

admin.site.register(models.Page, PageAdmin)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

    class Media:
        css = {
            'all': (
                'codemirror/lib/codemirror.css',
                'kopytka/css/editor.css',
            ),
        }
        js = (
            'codemirror/lib/codemirror.js',
            'codemirror/addon/mode/overlay.js',
            'codemirror/mode/xml/xml.js',
            'codemirror/mode/htmlmixed/htmlmixed.js',
            'codemirror/mode/django/django.js',
            'kopytka/js/editor.js',
            'kopytka/js/editor_template.js',
        )

admin.site.register(models.Template, TemplateAdmin)


class StyleSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    readonly_fields = ('output',)
    save_on_top = True

    class Media:
        css = {
            'all': (
                'codemirror/lib/codemirror.css',
                'kopytka/css/editor.css',
            ),
        }
        js = (
            'codemirror/lib/codemirror.js',
            'codemirror/mode/css/css.js',
            'kopytka/js/editor.js',
            'kopytka/js/editor_stylesheet.js',
        )

admin.site.register(models.StyleSheet, StyleSheetAdmin)
