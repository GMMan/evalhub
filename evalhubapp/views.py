from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

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
        context['expired'] = assignments.filter(expires_on__lt=now)

    return render(request, 'evalhubapp/evaluations.html', context)
