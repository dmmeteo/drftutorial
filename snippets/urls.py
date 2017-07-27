from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


# Adding optional format suffixes to our URLs
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    ## Functional-based urls:
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    
    ## Class-based urls:
    url(r'^snippets/$',
        views.SnippetListView.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetailView.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlightView.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        views.UserListView.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetailView.as_view(),
        name='user-detail'),
])


# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]