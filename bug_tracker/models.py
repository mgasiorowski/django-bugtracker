from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Bug(models.Model):
    title = models.CharField(max_length=200)
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
