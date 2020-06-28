from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Vacancy
from .forms import VacancyCreateForm


class VacancyList(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'


class VacancyCreateView(View):
    def post(self, request, *args, **kwargs):
        form = VacancyCreateForm(request.POST)
        if form.is_valid() and request.user.is_staff:
            clean_data = form.cleaned_data
            description = clean_data['description']
            Vacancy.objects.create(description=description, author=request.user)
            return HttpResponseRedirect('/home')
        raise PermissionDenied
