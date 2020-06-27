from django.shortcuts import render
from django.views.generic import ListView
from .models import Resume


class ResumeList(ListView):
    model = Resume
    template_name = 'resume_list.html'
