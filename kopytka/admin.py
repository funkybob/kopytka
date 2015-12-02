from django.contrib import admin

from . import models


class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'parent', 'order', 'template', 'is_published')
    list_filter = ('is_published',)
    ordering = ('parent', 'order',)

admin.site.register(models.Page, PageAdmin)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

admin.site.register(models.Template, TemplateAdmin)


class StyleSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    readonly_fields = ('output',)

admin.site.register(models.StyleSheet, StyleSheetAdmin)
