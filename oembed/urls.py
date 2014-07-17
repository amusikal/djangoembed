from django.conf import settings
from django.conf.urls import url
from oembed import views

urlpatterns = [
    url(r'^$', views.oembed_schema, name='oembed_schema'),
    url(r'^json/$', views.json, name='oembed_json'),
    url(r'^consume/json/$', views.consume_json, name='oembed_consume_json'),
    ]
