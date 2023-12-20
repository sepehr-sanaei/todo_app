from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.CreateTasksView.as_view(), name='tasks'),
    path('tasks/', views.TasksListView.as_view(), name='Tasks-List'),
    path('edit/<int:pk>/', views.EditTaskView.as_view(), name='edit-task'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete-task'),
    path('complete/<int:pk>/', views.TaskCompleteView.as_view(), name='complete-task'),
]