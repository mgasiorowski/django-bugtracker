from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

import re


class Project(models.Model):
    shortname = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(User)
    assigned_programmers = models.ManyToManyField(User, related_name='assigned_programmers', blank=True)
    assigned_testers = models.ManyToManyField(User, related_name='assigned_testers', blank=True)

    def validate_name_shortname(self):
        if self.name == '':
            raise Exception('name can not be an empty string.')
        if self.shortname == '':
            raise Exception('shortname can not be an emplty string.')
        alnum_re = re.compile(r'^\w+$')
        if not alnum_re.search(self.shortname):
            raise Exception("This value must contain only letters, numbers and underscores.")

    def save(self):
        self.validate_name_shortname()
        super(Project, self).save()

    def __unicode__(self):
        return self.shortname

    def get_absolute_url(self):
        return '/project/%s/' % self.shortname



class Bug(models.Model):
    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        unique=False,
        related_name='owner')
    assignee = models.ForeignKey(
        User,
        unique=False,
        related_name='assignee',
        null=True,
        blank=True)
    created_at = models.DateTimeField(
        'created_at',
        default=datetime.now)
    STATE_CHOICES = (
        ('open', 'open'),
        ('assigned', 'assigned'),
        ('closed', 'close'),
    )
    state = models.CharField(max_length=20, choices=STATE_CHOICES)

    LEVEL_CHOICES = (
        ('trival', 'trival'),
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
        ('critical', 'critical'),
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.title

    def delete(self):
        super(Bug, self).delete()

    def get_absolute_url(self):
        return '/taskdetails/%s/' % (self.id)

    def edit_url(self):
        return '/edittask/%s/' % (self.id)


class Comment(models.Model):
    text = models.TextField()
    bug = models.ForeignKey(Bug)
    owner = models.ForeignKey(User)
