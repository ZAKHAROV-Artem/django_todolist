from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', AllTasks.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_view'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('current/', CurrentTasks.as_view(), name='current_tasks'),
    path('completed/', CompletedTasks.as_view(), name='copmleted_tasks'),
]
