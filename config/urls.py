from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(settings.ADMIN_URL, include(admin.site.urls)),
]
