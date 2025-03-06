from tasks.apps import TasksConfig
from tasks.views import TaskAPIView
from django.urls import path

app_name = TasksConfig.name

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='tasks'),
]
