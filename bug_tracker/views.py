from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf

from django.views.generic import ListView, DetailView

from .models import Bug, Project

from django.views.generic.edit import CreateView, UpdateView


class BugList(ListView):
    template_name = 'bugs/bug_list.html'
    def get_queryset(self):
        project = Project.objects.get(shortname=self.kwargs['project_key'])
        return Bug.objects.filter(project=project)


class BugCreate(CreateView):
    model = Bug
    template_name = 'bugs/new_bug.html'
    fields = ['title', 'project', 'description', 'assignee', 'state', 'level']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BugCreate, self).form_valid(form)


class BugEdit(UpdateView):
    model = Bug
    template_name = 'bugs/new_bug.html'
    fields = ['title', 'project', 'description', 'assignee', 'state', 'level']


class ProjectList(ListView):
    template_name = 'bugs/project_list.html'
    model = Project


class BugsView(DetailView):
    template_name = 'bugs/bugs_view.html'

    def get_queryset(self):
        return Bug.objects.filter(pk=self.kwargs['pk'])
