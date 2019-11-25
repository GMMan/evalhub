from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

from survey.views.survey_completed import SurveyCompleted
from .models import SurveyAssignment


# Create your views here.


def index(request):
    return render(request, 'evalhubapp/index.html')


@login_required
def list_surveys(request):
    context = {
        'is_staff': request.user.is_staff
    }
    if not request.user.is_staff:
        now = timezone.now()
        assignments = SurveyAssignment.objects.filter(assignee__pk=request.user.pk)
        context['active'] = assignments.filter(completed_on__isnull=True)\
            .filter(Q(expires_on__gt=now)|Q(expires_on__isnull=True))
        context['completed'] = assignments.filter(completed_on__isnull=False)
        context['expired'] = assignments.filter(expires_on__lt=now, completed_on__isnull=True)

    return render(request, 'evalhubapp/evaluations.html', context)


@login_required
def begin_survey(request, assignment_id):
    assignment = SurveyAssignment.objects.get(pk=assignment_id)
    context = {}
    if assignment.assignee.pk != request.user.pk:
        context['error_message'] = 'You are not assigned to this evaluation.'
        return render(request, 'evalhubapp/evaluation_denied.html', context)

    if assignment.expires_on < timezone.now():
        context['error_message'] = 'The evaluation has expired.'
        return render(request, 'evalhubapp/evaluation_denied.html', context)

    request.session['assignment_id'] = assignment_id
    request.session['next'] = 'complete_evaluation'
    return redirect(assignment.survey)


@login_required
def complete_survey(request):
    context = {}
    if 'assignment_id' not in request.session:
        context['error_message'] = 'Invalid evaluation submission.'
        return render(request, 'evalhubapp/evaluation_denied.html', context)

    assignment = SurveyAssignment.objects.get(pk=request.session['assignment_id'])
    assignment.completed_on = timezone.now()
    assignment.save()

    del request.session['assignment_id']
    return render(request, 'evalhubapp/evaluation_complete.html', context)
