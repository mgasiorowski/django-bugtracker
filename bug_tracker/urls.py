from django.conf.urls import url

from views import BugList, ProjectList, BugsView, BugCreate, BugEdit

urlpatterns = [
    url(r'^$', ProjectList.as_view(), name='project_list'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^newbug/$', BugCreate.as_view(), name='new_bug'),
    url(r'^project/(?P<project_key>.*?)/$', BugList.as_view(), name='project'),
    url(r'^taskdetails/(?P<pk>.*?)/$', BugsView.as_view(), name='bug'),
    url(r'^editask/(?P<pk>\d+)/$', BugEdit.as_view(), name='bugs_edit')
]
