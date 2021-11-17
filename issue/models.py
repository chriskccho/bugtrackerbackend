from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)
    submitted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_submittedby')
    assigned_user = models.ManyToManyField(User, related_name='user_todo_project')

class Issue(models.Model):
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todo_issue')
    submitted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_submittedby')
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_issues")
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)