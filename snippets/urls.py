from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]


# -*- # # Adding urls detail format for ViewSets requests -*-
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
#
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'detail'
# })
#
#

# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])

# -*- Adding optional format suffixes to our URLs -*-
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     ## Functional-based urls:
#     # url(r'^snippets/$', views.snippet_list),
#     # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#
#     ## Class-based urls:
#     url(r'^snippets/$',
#         views.SnippetListView.as_view(),
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         views.SnippetDetailView.as_view(),
#         name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         views.SnippetHighlightView.as_view(),
#         name='snippet-highlight'),
#     url(r'^users/$',
#         views.UserListView.as_view(),
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         views.UserDetailView.as_view(),
#         name='user-detail'),
# ])


# # Login and logout views for the browsable API
# urlpatterns = [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]