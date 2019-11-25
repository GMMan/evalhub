from django.contrib.auth.models import AbstractUser
from django.db import models

from survey.models.survey import Survey

# Create your models here.


class User(AbstractUser):
    class Meta:
        app_label = 'evalhubapp'


class Evaluator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class DaycareUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    org_name = models.CharField(max_length=128, null=False, blank=False)
    invite_code = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.org_name


class SurveyAssignment(models.Model):
    assigner = models.ForeignKey(Evaluator, on_delete=models.SET_NULL, null=True)
    assignee = models.ForeignKey(DaycareUser, on_delete=models.CASCADE)
    completed_on = models.DateTimeField(null=True, blank=True)
    expires_on = models.DateTimeField(null=True, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=False, blank=False)

    @property
    def is_completed(self):
        return self.completed_on is not None
