from django.urls import path
from app_lesson_4.views import home

urlpatterns = [
    path('lesson_4', home, name='lesson_4'),
]