from django.conf.urls import url

from views import BugList, ProjectList, BugsView, BugCreate, BugEdit, ProjectUpdate, close_bug, AddComment

urlpatterns = [
    url(r'^$', ProjectList.as_view(), name='project_list'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^newbug/(?P<project_key>.*?)/$', BugCreate.as_view(), name='new_bug'),
    url(r'^project/(?P<project_key>.*?)/$', BugList.as_view(), name='project'),
    url(r'^taskdetails/(?P<pk>\d+)/$', BugsView.as_view(), name='bug'),
    url(r'^editask/(?P<pk>\d+)/$', BugEdit.as_view(), name='bugs_edit'),
    url(r'^project_update/(?P<project_key>.*?)/$', ProjectUpdate.as_view(), name='project_update'),
    url(r'^closetask/(?P<pk>\d+)/$', close_bug, name='close_bug'),
    url(r'^addcomment/(?P<pk>\d+)/$', AddComment.as_view(), name='add_comment'),
]
