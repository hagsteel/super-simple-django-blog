from django.conf.urls import patterns, url
from .views import BlogView, BlogListView, BlogListByTagView


urlpatterns = patterns(
    '',
    url(r'^$', BlogListView.as_view(), name='blog'),
    url(r'^tags/$', BlogListByTagView.as_view(), name='bloglist_by_tags'),
    url(r'^(?P<slug>[-\.\w]+)/$', BlogView.as_view(), name='blog_entry'),
)
