# kopytka
A modernised version of Gnocchi CMS

# Installing.

1. Install the package

1. Add installed apps

    INSTALLED_APPS = [
        ...
        'django.contrib.postgres',

        'kopytka',
    ]

1. Add template loader

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            ...
            'loaders': [
                'kopytka.loader.DBLoader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    ]

1. Add urls

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'', include('kopytka.urls', namespace='kopytka')),
    ]

