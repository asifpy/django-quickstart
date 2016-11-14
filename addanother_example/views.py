import django
from django.views import generic
from django.shortcuts import render

from django_addanother.views import CreatePopupMixin, UpdatePopupMixin

from .models import Team
from .forms import PlayerForm


class CreateTeam(CreatePopupMixin, generic.CreateView):
    model = Team
    fields = ['name']
    template_name = 'team_form.html'


class EditTeam(UpdatePopupMixin, generic.UpdateView):
    model = Team
    fields = ['name']
    template_name = 'team_form.html'