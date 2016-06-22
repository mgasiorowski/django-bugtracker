from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.project_list, name='project_list'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^newbug/$', views.new_bug, name='new_bug'),
    url(r'^project/(?P<project_key>.*?)/$', views.bug_list, name='project'),
    url(r'^taskdetails/(?P<id>.*?)/$', views.bugs_view, name='bug'),
    url(r'^editask/(?P<id>.*?)/$', views.bugs_edit, name='bugs_edit')
]
