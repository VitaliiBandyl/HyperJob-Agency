from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Resume
from .forms import ResumeCreateForm


class ResumeList(ListView):
    model = Resume
    template_name = 'resume/resume_list.html'


class ResumeCreateView(View):
    def post(self, request, *args, **kwargs):
        form = ResumeCreateForm(request.POST)
        if form.is_valid() and not request.user.is_staff:
            clean_data = form.cleaned_data
            description = clean_data['description']
            Resume.objects.create(description=description, author=request.user)
            return HttpResponseRedirect('/home')
        raise PermissionDenied

    def get(self, request, *args, **kwargs):
        raise PermissionDenied

