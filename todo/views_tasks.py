from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms.forms_tasks import TaskForm

class TaskCreateView(LoginRequiredMixin, View):
    # On get render the empty form
    def get(self, request):
        form = TaskForm()
        return render(request, 'todo/task_form.html', {'form': form, 'action': 'Create'})

    # On post save the form and redirect to the board
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()  # Save the task first
            task.assignees.set(form.cleaned_data['assignees'])  # Set the many-to-many relationship
            return redirect('todo:board')
        return render(request, 'todo/task_form.html', {'form': form, 'action': 'Create'})

class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'todo/task_form.html', {'form': form, 'action': 'Edit'})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:board')
        return render(request, 'todo/task_form.html', {'form': form, 'action': 'Edit'})

class TaskCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()
        return redirect('todo:board')
