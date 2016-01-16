from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^_/fragments/$', views.fragments, name='fragment-keys'),
    url(r'^css/(?P<name>[-\w]+)\.css$', views.style_sheet, name='style-sheet'),
    url(r'(?P<path>.*)$', views.page, name='page'),
]
