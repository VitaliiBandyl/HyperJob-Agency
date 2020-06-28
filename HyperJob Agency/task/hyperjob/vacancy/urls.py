from django.urls import path
from . import views

urlpatterns = [
    path('ies/', views.VacancyList.as_view()),
    path('y/new/', views.VacancyCreateView.as_view()),
]