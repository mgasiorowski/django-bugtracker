from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.bug_list, name='bugs'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^bugs/$', views.bug_list, name='bugs'),     
    url(r'^newbug/$', views.new_bug, name='new_bug'),
]
