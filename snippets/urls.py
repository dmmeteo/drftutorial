from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


## Class-based urls:
urlpatterns = [
    url(r'^snippets/$', views.SnippetListView.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailView.as_view()),
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view()),
    # REST Auth or in the end
    # url(r'^api-auth/', include('rest_framework.urls',
    #                            namespace='rest_framework')),
]

## Functional-based urls:
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# Adding optional format suffixes to our URLs
urlpatterns = format_suffix_patterns(urlpatterns)

# REST Auth
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

