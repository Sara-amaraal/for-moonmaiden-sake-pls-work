from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('choose-test/', views.list_test),   # Select test
    path('get_test/', views.get_test),  # Get info necessary to solve test
    path('grade_test/', views.grade_test)   # Test's grade and solutions
]
