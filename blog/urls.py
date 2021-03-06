#from django.conf.urls import url
from django.urls import path, re_path
from . import views
from .feeds import LatestPostsFeed

app_name = "blog"
urlpatterns = [
    #post views
    path('', views.post_list,name='post_list'),
    path('feeds', LatestPostsFeed(),name='post_feed'),
    #path('', views.PostListView.as_view() ,name='post_list'), #after adding class based PostListView() in view.py
    re_path(r'^tag/(?P<tag_slug>[\w-]+)/$',views.post_list, name='post_list_by_tag'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[-\w]+)/$',views.post_detail, name ='post_details'),
    re_path(r'^(?P<post_id>\d+)/share/$',views.post_share, name ='post_share')
]