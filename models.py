"""Mini Issue Tracker program. Originally taken from Paul Bissex's blog post:
http://news.e-scribe.com/230 and snippet: http://djangosnippets.org/snippets/28/
"""
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


STATUS_CODES = (
    (1, 'Open'),
    (2, 'Working'),
    (3, 'Closed'),
)

PRIORITY_CODES = (
    (1, 'Now'),
    (2, 'Soon'),
    (3, 'Someday'),
)

apps = [app for app in settings.INSTALLED_APPS if not app.startswith('django.')]


class Ticket(models.Model):
    """Trouble tickets"""
    title = models.CharField(max_length=100)
    project = models.CharField(blank=True, max_length=100, choices=list(enumerate(apps)))
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    submitter = models.ForeignKey(User, related_name="submitter")
    assigned_to = models.ForeignKey(User)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1, choices=STATUS_CODES)
    priority = models.IntegerField(default=1, choices=PRIORITY_CODES)

    class Meta:
        ordering = ('status', 'priority', 'submitted_date', 'title')

    def __unicode__(self):
        return self.title
