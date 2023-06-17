from django.urls import path

from . import views


urlpatterns = [
    path('v1/tests/create/', views.TestCreateView.as_view()),
    path('v1/tests/<str:login>/finish_iq/', views.IQTestUpdateView.as_view()),
    path('v1/tests/<str:login>/finish_eq/', views.EQTestUpdateView.as_view()),
    path('v1/tests/<str:login>/', views.TestRetrieveView.as_view()),
]
