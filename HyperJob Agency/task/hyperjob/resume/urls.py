from django.urls import path
from . import views


urlpatterns = [
    path('', views.ResumeList.as_view()),
]