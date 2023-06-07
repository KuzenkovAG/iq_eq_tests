from django.urls import path

from . import views


urlpatterns = [
    path('v1/tests/', views.test_create_view),
    path('v1/tests/<str:login>/finish_iq/', views.finish_iq_test),
    path('v1/tests/<str:login>/finish_eq/', views.finish_eq_test),
    path('v1/tests/<str:login>/', views.test_result_view),
]
