from django.urls import path
from .views import *

app_name = 'studentInfo'

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', student_form, name='student_add'),
    path('edit/<int:id>/', student_form, name='student_edit'),
    path('details/<int:id>/', student_details, name='student_details'),
]
