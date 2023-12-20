from django.shortcuts import redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from .models import Tasks
from .forms import TasksForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TasksListView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    queryset = Tasks.objects.all()
    context_object_name = 'tasks'
    template_name = "todo/tasks-list.html"
    

class CreateTasksView(LoginRequiredMixin, CreateView):
    login_url = 'accounts/login/'
    model = Tasks
    form_class = TasksForm
    success_url = "/tasks/"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditTaskView(LoginRequiredMixin,UpdateView):
    model = Tasks
    form_class = TasksForm
    success_url = "/tasks/"

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Tasks
    success_url = "/tasks/"
    
class TaskCompleteView(LoginRequiredMixin, View):
    model = Tasks
    success_url = "/tasks/"
    
    def get(self, request, *args, **kwargs):
        object = Tasks.objects.get(id=kwargs.get("pk"))
        object.task_complete = True
        object.save()
        return redirect(self.success_url)    