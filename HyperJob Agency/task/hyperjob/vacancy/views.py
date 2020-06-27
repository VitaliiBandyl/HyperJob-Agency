from django.shortcuts import render
from django.views.generic import ListView
from .models import Vacancy


class VacancyList(ListView):
    model = Vacancy
    template_name = 'vacancy_list.html'
