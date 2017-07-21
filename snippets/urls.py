from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


## Class-based urls:
urlpatterns = [
    url(r'^snippets/$', views.SnippetListView.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailView.as_view()),
]

## Functional-based urls:
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# Adding optional format suffixes to our URLs
urlpatterns = format_suffix_patterns(urlpatterns)
