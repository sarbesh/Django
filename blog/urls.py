#from django.conf.urls import url
from django.urls import path, re_path
from . import views

#app_name = "blog"
urlpatterns = [
    #post views
    #path('', views.post_list,name='post_list'),
    path('', views.PostListView.as_view() ,name='post_list'), #after adding class based PostListView() in view.py
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[-\w]+)/$',views.post_detail, name ='post_details'),
]