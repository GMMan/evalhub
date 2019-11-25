"""evalhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.utils.translation import ugettext_lazy

from evalhubapp import views as evalhub_views

# Set admin titles
admin.site.site_title = ugettext_lazy('EvalHub')
admin.site.site_header = ugettext_lazy('EvalHub admin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', evalhub_views.index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('evaluations/begin/<int:assignment_id>/', evalhub_views.begin_survey, name='begin_evaluation'),
    path('evaluations/completed/', evalhub_views.complete_survey, name='complete_evaluation'),
    path('evaluations/', evalhub_views.list_surveys, name='evaluations'),
]

if 'survey' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('evaluations/', include('survey.urls'))
    ]
