from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.CreateTasksView.as_view(), name='tasks'),
    path('tasks/', views.TasksListView.as_view(), name='Tasks-List')
]