from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from django.http import Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView

from .models import Bug, Project, Comment

from django.views.generic.edit import CreateView, UpdateView


def _can_update_project(user, project):
    return project.owner == user


def _can_add_bug(user, project):
    return project.owner == user or user in project.assigned_testers.all() or user in project.assigned_programmers.all()


def _can_close_bug(user, project):
    return project.owner == user or user in project.assigned_testers.all()


def _can_add_comment(user, project):
    return project.owner == user or user in project.assigned_testers.all() or user in project.assigned_programmers.all()


class BugList(ListView):
    template_name = 'bugs/bug_list.html'

    def get_queryset(self):
        self.project = Project.objects.get(shortname=self.kwargs['project_key'])
        return Bug.objects.filter(project=self.project)

    def get_context_data(self, **kwargs):
        context = super(BugList, self).get_context_data(**kwargs)
        context['project'] = self.project
        context['can_update_project'] = _can_update_project(user=self.request.user, project=self.project)
        context['can_add_bug'] = _can_add_bug(user=self.request.user, project=self.project)
        return context


class BugCreate(CreateView):
    model = Bug
    template_name = 'bugs/new_bug.html'
    fields = ['title', 'description', 'assignee', 'state', 'level']

    def dispatch(self, *args, **kwargs):
        self.project = Project.objects.get(shortname=self.kwargs['project_key'])
        if not _can_add_bug(user=self.request.user, project=self.project):
            raise Http404
        return super(BugCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.project = self.project
        return super(BugCreate, self).form_valid(form)


class BugEdit(UpdateView):
    model = Bug
    template_name = 'bugs/new_bug.html'
    fields = ['title', 'description', 'assignee', 'state', 'level']


class ProjectList(ListView):
    template_name = 'bugs/project_list.html'
    model = Project


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'bugs/project_update.html'
    fields = ['assigned_programmers', 'assigned_testers']

    def get_object(self):
        return self.project

    def dispatch(self, *args, **kwargs):
        self.project = Project.objects.get(shortname=self.kwargs['project_key'])
        if not _can_update_project(user=self.request.user, project=self.project):
            raise Http404
        return super(ProjectUpdate, self).dispatch(*args, **kwargs)


class BugsView(DetailView):
    template_name = 'bugs/bugs_view.html'

    def get_queryset(self):
        self.project = Project.objects.get(pk=self.kwargs['pk'])
        return Bug.objects.filter(project=self.project)

    def get_context_data(self, **kwargs):
        context = super(BugsView, self).get_context_data(**kwargs)
        context['project'] = self.project
        context['can_add_comment'] = _can_add_comment(user=self.request.user, project=self.project)
        return context


def close_bug(request, pk):
    bug = Bug.objects.get(pk=pk)
    if not _can_close_bug(user=request.user, project=bug.project):
        raise Http404
    bug.state = 'close'
    bug.save()
    return redirect('project', project_key=bug.project.shortname)


class AddComment(CreateView):
    model = Comment
    template_name = 'bugs/add_comment.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.bug = Bug.objects.get(pk=self.kwargs['pk'])
        form.instance.owner = self.request.user
        return super(AddComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('bug', kwargs={'pk': self.object.bug.pk})