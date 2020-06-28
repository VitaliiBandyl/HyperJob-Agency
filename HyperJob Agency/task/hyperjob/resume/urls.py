from django.urls import path
from . import views


urlpatterns = [
    path('s/', views.ResumeList.as_view()),
    path('/new/', views.ResumeCreateView.as_view()),
]